from pydantic import BaseModel

class AQIInput(BaseModel):
    pm25: float
    pm10: float
    temperature: float
    humidity: float
    wind_speed: float
    traffic: float