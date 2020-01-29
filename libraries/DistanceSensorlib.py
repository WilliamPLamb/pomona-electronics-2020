#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Wrapper library to help make connecting to and reading data from the HC-SR04 Ultrasonic range sensor easy. Intended function/example can be seen at bottom of file
   @author William Lamb
   @date 1/26/2020
   @email wpl12014@mymail.pomona.edu
   @version 0.0.1
"""
import RPi.GPIO as gpio
import time

class DistanceSensor:
    """A class to measure distance using the HC-SR04 Ultrasonic range Sensor. Code lovingly stolen/adapted from https://pythonprogramming.net/raspberry-pi-hc-sr04-programming"""

    # Initializes the classs with a trigger pin and echo pin for the Distance Sensor
    def __init__(self, trigPin, echoPin):
        # Pin number XX (like GPIOXX)
        self.trigPin = trigPin # Pin used to trigger reading the distance
        self.echoPin = echoPin # Pin used to read when distance signal comes back


    def distance(self, measure='cm'):
        try:
            gpio.setmode(gpio.BCM) # Sets up the board to use the GPIOXX pin numbering scheme
            gpio.setup(self.trigPin, gpio.OUT) # Sets up the trigPin as an output pin
            gpio.setup(self.echoPin, gpio.IN) # Sets up the echoPin as an input pin

            gpio.output(self.trigPin, False) # Turn the output pin off
            while gpio.input(self.echoPin) == 0: # Checks the input pin for the distance signal to return and measures the time
                nosig = time.time()

            while gpio.input(self.echoPin) == 1:
                sig = time.time()

            tl = sig - nosig

            # Converts time measurements to distace
            if measure == 'cm':
                distance = tl / 0.000058
            elif measure == 'in':
                distance = tl / 0.000148
            else:
                print('improper choice of measurement: in or cm')
                distance = None

            gpio.cleanup() # Cleans up inputs and outputs on pins
            return distance
        except:
            distance = 100 # If you get a distance of 100, something's wrong
            gpio.cleanup()
            return distance


if __name__ == "__main__":
    test = DistanceSensor(17, 27) # Initialize the class with trigPin as GPIO17, and echoPin as GPIO27

    while(True): # Get distance measurement every 2 seconds
        print(test.distance('cm'))

        time.sleep(1.0) # Sleep for 2 seconds
