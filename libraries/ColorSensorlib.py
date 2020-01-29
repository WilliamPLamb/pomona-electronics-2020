#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Wrapper library to help make connecting to and reading data from TCS34725 color sensor easy. Intended function/example can be seen at bottom of file
   @author William Lamb
   @date 1/23/2020
   @email wpl12014@mymail.pomona.edu
   @version 0.0.1
"""
import board
import busio
import time
import adafruit_tcs34725



class ColorSensor:
    """A class to measure color using the TCS34725 RGB Color Sensor. Code lovingly stolen/adapted from https://learn.adafruit.com/adafruit-color-sensors/python-circuitpython"""

    # Initializes class with the i2c communication connection using the board's SDA line on board pin 3 (GPIO pin 2) and SCL line on board pin 5 (GPIO pin 3)
    def __init__(self, i2c):
        self.sensor = adafruit_tcs34725.TCS34725(i2c)

    # Checks and returns the sensor's RGB color it's currently reading
    def getRGB(self):
        return self.sensor.color_rgb_bytes

    # Checks and returns the sensor's color tempurature reading
    def getColorTemperature(self):
        return self.sensor.color_temperature

    # Checks and returns the sensor's lux reading (apparently often not that accurate)
    def getLux(self):
        return self.sensor.lux

    # Sets the sensor's integration time in ms
    # Must be a value between 2.4 and 614.4
    # Will return the same value if it worked, and None if it didn't
    def setIntegrationTime(self, integrationTimeParam):
        if(integrationTimeParam > 2.4 and integrationTimeParam < 614.4):
            self.sensor.integration_time = integrationTimeParam
            return integrationTimeParam
        else:
            return None

    # Sets the sensor gain value
    # Must be a value of 1, 4, 16, or 60
    # Will return the same value if it worked, and None if it didn't
    def setSensorGain(self, sensorGainParam):
        if(sensorGainParam == 1 or sensorGainParam == 4 or sensorGainParam == 16 or sensorGainParam == 60):
            self.sensor.gain = sensorGainParam
            return sensorGainParam
        else:
            return None









if __name__ == "__main__":

    i2c = busio.I2C(board.SCL, board.SDA) # Initializes the i2c connection on the Raspberry Pi
    test = ColorSensor(i2c) # Initializes the color sensor with the i2c connection

    while(True): # Get measurements every second

        R, G, B = test.getRGB()
        print('Color: ({0}, {1}, {2})'.format(R, G, B)) # Reads RGB from the sensor
        print('Temperature: {0}K'.format(test.getColorTemperature())) # Reads Color Temperature from the sensor
        print('Lux: {0}'.format(test.getLux())) # Reads Lux from the sensor

        time.sleep(1.0) # Sleep for 1 second
