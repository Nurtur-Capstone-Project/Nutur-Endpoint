from fastapi import FastAPI, File, UploadFile, Response
import uvicorn
from PIL import Image
import numpy as np
import tensorflow as tf
import traceback
import time

model = tf.keras.models.load_model('./ResNet50V2_Model.h5')
app = FastAPI()


@app.get("/")
async def index():
    return "This is nurtur!"


@app.post("/")
async def predict(file: UploadFile = File(...)):
    try:
        image = Image.open(file.file)
        image = np.asarray(image.resize((224, 224)))
        # image = image/*apakah modelnya terdapat preprocessing normalization ?. if true (image/255), if else (null).
        image = (image/255)
        image = np.expand_dims(image, 0)

        start_time = time.time()
        result = model.predict(image)
        end_time = time.time()
        prediction = np.argmax(result)
        time_predict = round(end_time - start_time, 2)

        accuracy = np.max(result)

        if prediction == 0:
            return {
                'id': '1',
                'name' : 'angry',
                "accuracy": float(accuracy),
                "time_predict": float(time_predict),
                }
        elif prediction == 1:
            return {
                'id': '2',
                'name':'disgust',
                "accuracy": float(accuracy),
                "time_predict": float(time_predict)
                }

        elif prediction == 2:
            return {
                'id': '3',
                'name':'fear',
                "accuracy": float(accuracy),
                "time_predict": float(time_predict)
                }
        elif prediction == 3:
            return {
                'id': '4',
                'name':'happy',
                "accuracy": float(accuracy),
                "time_predict": float(time_predict)
                }
        elif prediction == 4:
            return {
                'id': '5',
                'name':'neutral',
                "accuracy": float(accuracy),
                "time_predict": float(time_predict)
                }
        elif prediction == 5:
            return {
                'id': '6',
                'name':'Sadness',
                "accuracy": float(accuracy),
                "time_predict": float(time_predict)
                }
        elif prediction == 6:
            return {
                'id': '7',
                'name':'surprise',
                "accuracy": float(accuracy),
                "time_predict": float(time_predict)
                }


    except Exception as e:
        traceback.print_exc()
        return {"message": "Internal Server Error"}


if __name__ == '_main_':
    port = 8001
    print(f"Listening to http://0.0.0.0:{port}")
    uvicorn.run(app, host='0.0.0.0', port=port)

