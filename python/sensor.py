#!/usr/bin/python -u
# https://gist.github.com/kadamski/92653913a53baf9dd1a8

import time, json

from sds011 import SDS011
from bmp280 import BMP280

JSON_FILE = '/var/www/html/sensor.json'

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus


if __name__ == "__main__":

    aqi = SDS011("/dev/ttyUSB0", use_query_mode=True)

    bus = SMBus(1)
    bmp280 = BMP280(i2c_dev=bus)
    time.sleep(5) # we need this to minimaze spikes after rpi starts

    while True:
        aqi.sleep(sleep=0) #Work
        for t in range(6):
            values = aqi.query();
            temperature = bmp280.get_temperature()
            pressure = bmp280.get_pressure()

            if values is not None and len(values) == 2:
              print("PM2.5:", values[0], ", PM10:", values[1], ', T: {:05.2f}°C,  P: {:05.2f} hPa'.format(temperature, pressure))
              time.sleep(5)

        # open stored data
        try:
            with open(JSON_FILE) as json_data:
                data = json.load(json_data)
        except IOError as e:
            data = []

        # check if length is more than 100 and delete first element
        if len(data) > 100:
            data.pop(0)

        # append new values
        jsonrow = {'pm25': values[0], 'pm10': values[1], 't': '{:05.2f}'.format(temperature), 'p': '{:05.2f}'.format(pressure),
                      'time': time.strftime("%d.%m.%Y %H:%M:%S")}
        data.append(jsonrow)

        # save it
        with open(JSON_FILE, 'w') as outfile:
            json.dump(data, outfile)

        print("Going to sleep for 150 sec...")
        aqi.sleep()
        time.sleep(150)
        
