import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

data = pd.read_csv("data/aqi_data.csv")

X = data[['PM2.5', 'PM10', 'temperature', 'humidity', 'wind_speed']]
y = data['AQI']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

joblib.dump(model, 'model/aqi_model.pkl')

print("Model trained successfully")