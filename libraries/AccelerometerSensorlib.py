#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Wrapper library to help make connecting to and reading data from MMA8451 accelerometer easy. Intended function/example can be seen at bottom of file
   @author William Lamb
   @date 1/23/2020
   @email wpl12014@mymail.pomona.edu
   @version 0.0.1
"""
import board
import busio
import time
import adafruit_mma8451




class AccelerometerSensor:
    """A class to measure acceleration using the MMA451 Acceleromter Sensor. Code lovingly stolen/adapted from https://learn.adafruit.com/adafruit-mma8451-accelerometer-breakout/python-circuitpython"""

    # Initializes class with the i2c communication connection using the board's SDA line on board pin 3 (GPIO pin 2) and SCL line on board pin 5 (GPIO pin 3)
    # Automatically assume address is 0x1C, but can change if necessary
    # TODO: fix i2c addressing
    def __init__(self, i2c, addressParam=0x1d):

        time.sleep(2) # ...Apparently the sleep is necessary...not for anything else, though...
        self.sensor = adafruit_mma8451.MMA8451(i2c, addressParam)

    # Checks and returns the sensor's acceleration reading as a tuple of (x,y,z) values
    def getAcceleration(self):
        return self.sensor.acceleration

    # Checks and returns the sensor's orientation reading
    def getOrientation(self):
        return self.sensor.orientation

    # Sets the sensor's acceleration range in +-G
    # Must be a value of 2, 4, or 8
    # Will return the same value if it worked, and None if it didn't
    def setAccelerationRange(self, rangeParam):
        if(rangeParam == 2):
            self.sensor.range = adafruit_mma8451.RANGE_2G
            return rangeParam
        elif(rangeParam == 4):
            self.sensor.range = adafruit_mma8451.RANGE_4G
            return rangeParam
        elif(rangeParam == 8):
            self.sensor.range = adafruit_mma8451.RANGE_8G
            return rangeParam
        else:
            return None

    # Sets the rate at which the sensor measures acceleration data (in Hz)
    # Must be a value of 1.56, 6.25, 12.5, 50, 100, 200, 400, or 800
    # Will return the same value if it worked, and None if it didn't
    def setDataRate(self, dataRateParam):
        if(dataRateParam == 1.56):
            self.sensor.data_rate = adafruit_mma8451.DATARATE_1_56HZ
            return dataRateParam
        elif(dataRateParam == 6.25):
            self.sensor.data_rate = adafruit_mma8451.DATARATE_6_25HZ
            return dataRateParam
        elif(dataRateParam == 12.5):
            self.sensor.data_rate = adafruit_mma8451.DATARATE_12_5HZ
            return dataRateParam
        elif(dataRateParam == 50):
            self.sensor.data_rate = adafruit_mma8451.DATARATE_50HZ
            return dataRateParam
        elif(dataRateParam == 100):
            self.sensor.data_rate = adafruit_mma8451.DATARATE_100HZ
            return dataRateParam
        elif(dataRateParam == 200):
            self.sensor.data_rate = adafruit_mma8451.DATARATE_200HZ
            return dataRateParam
        elif(dataRateParam == 400):
            self.sensor.data_rate = adafruit_mma8451.DATARATE_400HZ
            return dataRateParam
        elif(dataRateParam == 800):
            self.sensor.data_rate = adafruit_mma8451.DATARATE_800HZ
            return dataRateParam
        else:
            return None









if __name__ == "__main__":

    i2c = busio.I2C(board.SCL, board.SDA) # Initializes the i2c connection on the Raspberry Pi
    test = AccelerometerSensor(i2c) # Initializes the color sensor with the i2c connection

    while(True): # Get measurements every second
        x, y, z = test.getAcceleration() # Gets x, y, and z acceleration from the sensor
        print('Acceleration: x={0:0.3f}m/s^2 y={1:0.3f}m/s^2 z={2:0.3f}m/s^2'.format(x, y, z))

        orientation = test.getOrientation() # Gets orientation from the sensor
        # Orientation is one of these values:
        #  - PL_PUF: Portrait, up, front
        #  - PL_PUB: Portrait, up, back
        #  - PL_PDF: Portrait, down, front
        #  - PL_PDB: Portrait, down, back
        #  - PL_LRF: Landscape, right, front
        #  - PL_LRB: Landscape, right, back
        #  - PL_LLF: Landscape, left, front
        #  - PL_LLB: Landscape, left, back
        print('Orientation: ', end='')
        if orientation == adafruit_mma8451.PL_PUF:
            print('Portrait, up, front')
        elif orientation == adafruit_mma8451.PL_PUB:
            print('Portrait, up, back')
        elif orientation == adafruit_mma8451.PL_PDF:
            print('Portrait, down, front')
        elif orientation == adafruit_mma8451.PL_PDB:
            print('Portrait, down, back')
        elif orientation == adafruit_mma8451.PL_LRF:
            print('Landscape, right, front')
        elif orientation == adafruit_mma8451.PL_LRB:
            print('Landscape, right, back')
        elif orientation == adafruit_mma8451.PL_LLF:
            print('Landscape, left, front')
        elif orientation == adafruit_mma8451.PL_LLB:
            print('Landscape, left, back')


        time.sleep(1.0) # Sleep for 1 second
