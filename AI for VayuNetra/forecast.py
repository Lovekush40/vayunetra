import joblib

model = joblib.load('model/aqi_model.pkl')

def predict_aqi(pm25, pm10, temp, humidity, wind):
    prediction = model.predict([[pm25, pm10, temp, humidity, wind]])
    return prediction[0]