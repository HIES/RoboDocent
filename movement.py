from Adafruit_MotorHAT import Adafruit_MotorHAT
import time
import atexit

MoHat = Adafruit_MotorHAT()

MotorLeft = MoHat.getMotor(2)
MotorRight = MoHat.getMotor(1)

MOTOR_SPEED = 100
MotorLeft.setSpeed(MOTOR_SPEED)
MotorRight.setSpeed(MOTOR_SPEED)
    
def turn_off_motors():
    MotorLeft.run(MoHat.RELEASE)
    MotorRight.run(MoHat.RELEASE)
        
def drive_forwards():
    MotorLeft.run(MoHat.FORWARD)
    MotorRight.run(MoHat.FORWARD)
        
def drive_backwards():
    MotorLeft.run(MoHat.BACKWARD)
    MotorRight.run(MoHat.BACKWARD)

        
def drive_left():
    MotorLeft.run(MoHat.RELEASE)
    MotorRight.run(MoHat.FORWARD)
def drive_right():
    MotorLeft.run(MoHat.FORWARD)
    MotorRight.run(MoHat.RELEASE)
def pivot_turn():
    MotorLeft.run(MoHat.FORWARD)
    MotorRight.run(MoHat.BACKWARD)
def slight_left():
    MotorLeft.setSpeed(70)
    MotorRight.setSpeed(100)
    MotorLeft.run(MoHat.FORWARD)
    MotorRight.run(MoHat.FORWARD)
    MotorLeft.setSpeed(MOTOR_SPEED)
    MotorRight.setSpeed(MOTOR_SPEED)

def slight_right():
    MotorLeft.setSpeed(100)
    MotorRight.setSpeed(70)
    MotorLeft.run(MoHat.FORWARD)
    MotorRight.run(MoHat.FORWARD)
    MotorLeft.setSpeed(MOTOR_SPEED)
    MotorRight.setSpeed(MOTOR_SPEED)
        
