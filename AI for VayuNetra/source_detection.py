def detect_source(pm25, traffic, wind_speed):
    if pm25 > 150 and traffic > 80 and wind_speed < 5:
        return "Traffic Pollution Hotspot"

    elif pm25 > 150 and traffic < 40:
        return "Industrial Pollution"

    else:
        return "Mixed Pollution Source"