# Servo Control
import RPi.GPIO as gpio
import time


class ServoController:

    def __init__(self, controlPinParam, HzParam=50, neutralDutyCyclePercentParam=7.5, maxCWDutyCyclePercentParam=10.0, maxCCWDutyCyclePercentParam=5.0):
        # Pin number XX (like GPIOXX)
        gpio.setmode(gpio.BCM) # Sets up the board to use the GPIOXX pin numbering scheme
        # Needs to be a PWM pin
        self.controlPin = controlPinParam
        # Setup pin for output
        gpio.setup(self.controlPin, gpio.OUT)
        # Set up PWM (throw error if not PWM pin)
        self.isSetupCorrectly = False
        self.pwm = None
        try:
            self.pwm = gpio.PWM(self.controlPin, HzParam)
            self.isSetupCorrectly = True
        except:
            # Setup didn't work, something's wrong
            self.isSetupCorrectly = False

        # Save duty cycle variables for stopping, moving clockwise, and moving counterclockwise
        self.neutralDutyCycle = neutralDutyCyclePercentParam
        self.maxCWDutyCycle = maxCWDutyCyclePercentParam
        self.maxCCWDutyCycle = maxCCWDutyCyclePercentParam
        self.currentDutyCycle = self.neutralDutyCycle
        # Start your engines!
        if(self.isSetupCorrectly):
            # Start PWM pin with no servo movement
            self.pwm.start(self.neutralDutyCycle)


    def getIsSetupCorrectly(self):
        return self.isSetupCorrectly

    def ccw(self, speedParam):
        if(self.isSetupCorrectly):
            self.currentDutyCycle = self.neutralDutyCycle + (self.maxCCWDutyCycle - self.neutralDutyCycle)*speedParam/100
            self.pwm.ChangeDutyCycle(self.currentDutyCycle)

    def cw(self, speedParam):
        if(self.isSetupCorrectly):
            self.currentDutyCycle = self.neutralDutyCycle + (self.maxCWDutyCycle - self.neutralDutyCycle)*speedParam/100
            self.pwm.ChangeDutyCycle(self.currentDutyCycle)

    def stop(self):
        if(self.isSetupCorrectly):
            self.currentDutyCycle = self.neutralDutyCycle
            self.pwm.ChangeDutyCycle(self.currentDutyCycle)

class DrivingController:

    # Ignore all the parameters besides the servoCWPinParam and servoCCWPinParam. The others are just to be able to use this code with servos that use different cycle times and duty cycle percents for neutral, clockwise, and counterclockwise
    def __init__(self, servoCWPinParam, servoCCWPinParam, HzCWParam=50, neutralDutyCyclePercentCWParam=7.5, maxCWDutyCyclePercentCWParam=10.0, maxCCWDutyCyclePercentCWParam=5.0, HzCCWParam=50, neutralDutyCyclePercentCCWParam=7.5, maxCWDutyCyclePercentCCWParam=10.0, maxCCWDutyCyclePercentCCWParam=5.0):
        # Pin number XX (like GPIOXX)
        gpio.setmode(gpio.BCM) # Sets up the board to use the GPIOXX pin numbering scheme
        # Needs to be a PWM pin
        self.cwServo = ServoController(servoCWPinParam, HzCWParam, neutralDutyCyclePercentCWParam, maxCWDutyCyclePercentCWParam, maxCCWDutyCyclePercentCWParam)
        self.ccwServo = ServoController(servoCCWPinParam, HzCCWParam, neutralDutyCyclePercentCCWParam, maxCWDutyCyclePercentCCWParam, maxCCWDutyCyclePercentCCWParam)
        time.sleep(2)
        self.isSetupCorrectly = self.cwServo.getIsSetupCorrectly() and self.ccwServo.getIsSetupCorrectly()

    def getIsSetupCorrectly(self):
        return self.isSetupCorrectly

    def forward(self, speedParamCW, speedParamCCW=None):
        if(self.isSetupCorrectly):
            # Only need to set one speed for forwards and backwards
            if(speedParamCCW is None):
                speedParamCCW = speedParamCW
            self.cwServo.cw(speedParamCW)
            self.ccwServo.ccw(speedParamCCW)

    def backward(self, speedParamCW, speedParamCCW=None):
        if(self.isSetupCorrectly):
            # Only need to set one speed for forwards and backwards
            if(speedParamCCW is None):
                speedParamCCW = speedParamCW
            self.cwServo.ccw(speedParamCW)
            self.ccwServo.cw(speedParamCCW)

    def turnLeft(self, speedParamCW, speedParamCCW=None):
        if(self.isSetupCorrectly):
            # Only need to set one speed for forwards and backwards
            if(speedParamCCW is None):
                speedParamCCW = speedParamCW
            self.cwServo.cw(speedParamCW)
            self.ccwServo.cw(speedParamCCW)

    def turnRight(self, speedParamCW, speedParamCCW=None):
        if(self.isSetupCorrectly):
            # Only need to set one speed for forwards and backwards
            if(speedParamCCW is None):
                speedParamCCW = speedParamCW
            self.cwServo.ccw(speedParamCW)
            self.ccwServo.ccw(speedParamCCW)

    def stop(self):
        if(self.isSetupCorrectly):
            self.cwServo.stop()
            self.ccwServo.stop()



if __name__ == "__main__":

    testIndividualServos = True

    servo1PWMPin = 18
    servo2PWMPin = 13

    try:
        if(testIndividualServos):
            servo1Test = ServoController(servo1PWMPin)# Initialize the class with control PWM pin as GPIO18
            servo2Test = ServoController(servo2PWMPin)# Initialize the class with control PWM pin as GPIO13

            if(servo1Test.getIsSetupCorrectly()):
                servo1Test.stop()
                time.sleep(2)
                # Test CW motion
                servo1Test.cw(20)
                time.sleep(2)
                servo1Test.cw(50)
                time.sleep(2)
                servo1Test.cw(100)
                time.sleep(2)
                servo1Test.stop()
                time.sleep(2)
                # Test CCW motion
                servo1Test.ccw(20)
                time.sleep(2)
                servo1Test.ccw(50)
                time.sleep(2)
                servo1Test.ccw(100)
                time.sleep(2)

                servo1Test.stop()
                time.sleep(2)
            else:
                print("Servo 1 not set up correctly")

            if(servo2Test.getIsSetupCorrectly()):
                servo2Test.stop()
                time.sleep(2)
                # Test CW motion
                servo2Test.cw(20)
                time.sleep(2)
                servo2Test.cw(50)
                time.sleep(2)
                servo2Test.cw(100)
                time.sleep(2)
                servo2Test.stop()
                time.sleep(2)
                # Test CCW motion
                servo2Test.ccw(20)
                time.sleep(2)
                servo2Test.ccw(50)
                time.sleep(2)
                servo2Test.ccw(100)
                time.sleep(2)

                servo2Test.stop()
                time.sleep(2)
            else:
                print("Servo 2 not set up correctly")

        else:
            twoMotors = DrivingController(servo1PWMPin,servo2PWMPin)

            if(twoMotors.getIsSetupCorrectly()):
                twoMotors.stop()
                time.sleep(2)
                # Test CW motion
                twoMotors.forward(20)
                time.sleep(2)
                twoMotors.forward(50)
                time.sleep(2)
                twoMotors.forward(100)
                time.sleep(2)
                twoMotors.stop()
                time.sleep(2)
                # Test CCW motion
                twoMotors.backward(20)
                time.sleep(2)
                twoMotors.backward(50)
                time.sleep(2)
                twoMotors.backward(100)
                time.sleep(2)
                # Test turning
                twoMotors.turnLeft(50)
                time.sleep(2)
                twoMotors.turnRight(50)
                time.sleep(2)

                twoMotors.stop()
                time.sleep(2)
            else:
                print("Both motors not set up correctly")
    finally:
        gpio.cleanup()
