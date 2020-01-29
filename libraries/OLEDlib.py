#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Wrapper library to help make connecting to and writing text to OLED display easy. Intended function/example can be seen at bottom of file
   @author William Lamb
   @date 1/23/2020
   @email wpl12014@mymail.pomona.edu
   @version 0.0.1
"""
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time
import RPi.GPIO as GPIO


class OLED:
    """A class to control the OLED over i2c. Code lovingly stolen/adapted from https://tech.scargill.net/ssd1306-with-python/ and https://learn.adafruit.com/monochrome-oled-breakouts/python-setup"""

    # Initializes class with the i2c communication connection using the board's SDA line on board pin 3 (GPIO pin 2) and SCL line on board pin 5 (GPIO pin 3)
    def __init__(self, i2c, addressParam=0x3c):
        # Define width and height of our specific OLED
        self.width = 128
        self.height= 64
        self.image = Image.new('1', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.load_default()

        # Connect to the board
        self.oled = adafruit_ssd1306.SSD1306_I2C(self.width, self.height, i2c, addr=addressParam)
        GPIO.setmode(GPIO.BCM)

        # Define line and column numbers of our specific OLED
        self.line1 = 2
        self.line2 = 11
        self.line3 = 20
        self.line4 = 29
        self.line5 = 38
        self.line6 = 47

        self.col1 = 4

    # Clean up pins when done with class. May throw unexpected behavior based on when garbage cleanup happens
    def __del__(self):
        GPIO.cleanup()

    # Clear display and saved image
    def clear(self):
        self.clearSavedImage()
        self.oled.fill(0)
        self.oled.show()

    # Clear saved image, so not overlaying new text over old text
    def clearSavedImage(self):
        self.image = Image.new('1', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)

    # Write some text to the screen
    def drawText(self, textParam="Hello World!", xPosParam=None, yPosParam=None, fillParam=255):
        if(xPosParam is None):
            xPosParam = self.col1
        if(yPosParam is None):
            yPosParam = self.line1
        try:
            self.draw.text((xPosParam, yPosParam), textParam, font=self.font, fill = fillParam)
            # self.oled.image(self.image)
        except:
            return None
        return None

    # Draw an image, and if no image is selected, draw internal image
    def drawImage(self, imageParam=None):
        if(imageParam is None):
            self.oled.image(self.image)
        else:
            try:
                self.oled.image(imageParam)
            except:
                return None
        return None

    # Show the saved image (and text) on the OLED screen
    def showDisplay(self):
        self.oled.image(self.image)
        self.oled.show()
        return None

    # Load in a font to use
    def loadFont(self, fontParam = 'default'):
        # if no font is loaded, use default font
        if (fontParam is 'default'):
            self.font = ImageFont.load_default()
        else:
            # Try loading font from memory
            try:
                return None
            # Font did not load correctly
            except:
                return None







if __name__ == "__main__":

    i2c = busio.I2C(board.SCL, board.SDA) # Initializes the i2c connection on the Raspberry Pi
    oled = OLED(i2c) # Initializes the OLED with the i2c connection

    oled.drawText() # Try drawing some text to the internal saved image
    oled.showDisplay() # Show the internal saved image (and text) on the OLED display
    time.sleep(5)
    oled.clear() # Clear the internal saved image and the OLED display
    time.sleep(1)
    oled.drawText("Test") # Try drawing some text to the internal saved image
    oled.showDisplay() # Show the internal saved image (and text) on the OLED display
    time.sleep(5)
    oled.clear() # Clear the internal saved image and the OLED display
    time.sleep(1)








    
    # What usage without wrapper library might normally look like

    # # Create a blank image
    # image = Image.new('1', (oled.width, oled.height))
    #
    # font = ImageFont.load_default()
    #
    # text = "Hello World!"
    #
    # # Draw something
    #
    # try:
    # 	while(True):
    # 		oled.fill(0)
    # 		draw = ImageDraw.Draw(image)
    # 		draw.rectangle((0,0, WIDTH - 1, HEIGHT - 1), outline="white",fill="black")
    # 		draw.text((col1, line1), text, font=font, fill = 255)
    # 		draw.text((col1, line3), 'GPIO 4:', font=font, fill=255)
    # 		draw.text((col1, line4), str(GPIO.input(INPUTPIN)), font=font,fill=255)
    # 		oled.image(image)
    # 		oled.show()
    # 		time.sleep(0.2)
    #
    # finally:
    # 	GPIO.cleanup()
