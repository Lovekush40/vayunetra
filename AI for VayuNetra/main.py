from fastapi import FastAPI
from schemas import AQIInput
from forecast import predict_aqi
from source_detection import detect_source

app = FastAPI()

@app.post("/predict")
def predict(data: AQIInput):
    aqi = predict_aqi(
        data.pm25,
        data.pm10,
        data.temperature,
        data.humidity,
        data.wind_speed
    )

    source = detect_source(
        data.pm25,
        data.traffic,
        data.wind_speed
    )

    return {
        "predicted_aqi": aqi,
        "source": source
    }



from fastapi import FastAPI

app = FastAPI()

@app.get("/predict")
def predict():
    return {
        "sklearn_prediction": 287,
        "tensorflow_forecast": [290,295,300,302,310,315,320],
        "pytorch_anomaly": "No anomaly"
    }