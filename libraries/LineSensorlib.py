#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Wrapper library to help make connecting to and reading data from the MH Sensor Series line sensor easy. Intended function/example can be seen at bottom of file
   @author William Lamb
   @date 1/26/2020
   @email wpl12014@mymail.pomona.edu
   @version 0.0.1
"""
import RPi.GPIO as gpio
import time

class LineSensor:
    """A class to measure lines using the MH Sensor Series"""

    # Initializes the class with the pin used to read from the Line Sensor
    def __init__(self, readPin):
        self.readPin = readPin # Pin number XX (like GPIOXX)

    def readLine(self):
        gpio.setmode(gpio.BCM) # Sets up the board to use the GPIOXX pin numbering scheme
        gpio.setup(self.readPin, gpio.IN) # Sets up the readPin as an input pin
        output = gpio.input(self.readPin) # Actually reads from the input pin
        gpio.cleanup() # Cleans up any inputs or outputs on the pins
        return output # Returns the state of the readPin

if __name__ == "__main__":
    readPin = 22
    test = LineSensor(readPin) # Initialize the class with readPin as GPIO17

    while(True): # Get data every 1 second
        print(test.readLine())

        time.sleep(1) # Sleep for 1 second
