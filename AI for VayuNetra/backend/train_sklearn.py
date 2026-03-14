import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

data = pd.read_csv("data/aqi_data.csv")

X = data[['PM2.5','PM10','temperature','humidity','wind_speed']]
y = data['AQI']

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "model/sklearn_model.pkl")