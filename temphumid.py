import dht

def temphumid(pin):

    sensor = dht.DHT11(pin)

    sensor.measure()
    temperature  = sensor.temperature()
    humidity = sensor.humidity()

    return temperature, humidity