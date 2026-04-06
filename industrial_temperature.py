def trigger_alarm(temperatures, threshold=80):
    sensores_alerta = []

    for sensor, temp in temperatures.items():
        if temp > threshold:
            sensores_alerta.append(sensor)

    return sensores_alerta