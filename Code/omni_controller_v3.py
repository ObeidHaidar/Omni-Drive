from math import cos, pi, radians
import time
import RPi.GPIO as GPIO

# Setup the pins
MOTOR1L = 20
MOTOR1R = 21
MOTOR1PWM = 16

MOTOR2L = 26
MOTOR2R = 19
MOTOR2PWM = 13

MOTOR3R = 5
MOTOR3L = 6
MOTOR3PWM = 12

MOTORPWMFREQUENCY = 50  # IN Hz

# Define pins as outputs
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(MOTOR1L, GPIO.OUT)
GPIO.setup(MOTOR1R, GPIO.OUT)
GPIO.setup(MOTOR1PWM, GPIO.OUT)
GPIO.setup(MOTOR2L, GPIO.OUT)
GPIO.setup(MOTOR2R, GPIO.OUT)
GPIO.setup(MOTOR2PWM, GPIO.OUT)
GPIO.setup(MOTOR3L, GPIO.OUT)
GPIO.setup(MOTOR3R, GPIO.OUT)
GPIO.setup(MOTOR3PWM, GPIO.OUT)

# Set motor PWM
en01 = GPIO.PWM(MOTOR1PWM, MOTORPWMFREQUENCY)
en01.start(0)
en02 = GPIO.PWM(MOTOR2PWM, MOTORPWMFREQUENCY)
en02.start(0)
en03 = GPIO.PWM(MOTOR3PWM, MOTORPWMFREQUENCY)
en03.start(0)

# Determines cos of an angle in radians
def dcos(a):
    return cos(radians(a))


# Set motor 1 velocity
def motor1(value):
    if value < 0 and value >= -100:
        motor1r = 0
        motor1l = 1
        motor1speed = abs(value)
        print('Motor1 is rotating CCW')
    elif value > 0 and value <= 100:
        motor1r = 1
        motor1l = 0
        motor1speed = abs(value)
        print('Motor1 is rotating CW')
    elif value == 0:
        motor1r = 0
        motor1l = 0
        motor1speed = 0
        print('Motor1 is not rotating')
    elif value < -100 or value > 100:
        print('error')
        # come back and do changes here
    en01.ChangeDutyCycle(motor1speed)
    GPIO.output(MOTOR1L, motor1l)
    GPIO.output(MOTOR1R, motor1r)

# Set motor 3 velocity
def motor3(value):
    if value < 0 and value >= -100:
        motor2r = 0
        motor2l = 1
        motor2speed = abs(value)
        print('Motor2 is rotating CCW')
    if value > 0 and value <= 100:
        motor2r = 1
        motor2l = 0
        motor2speed = abs(value)
        print('Motor2 is rotating CW')
    if value == 0:
        motor2r = 0
        motor2l = 0
        motor2speed = 0
        print('Motor2 is not rotating')
    if value < -100 or value > 100:
        print('error')
        # come back and do changes here
    en02.ChangeDutyCycle(motor2speed)
    GPIO.output(MOTOR2L, motor2l)
    GPIO.output(MOTOR2R, motor2r)


# Set motor 2 velocity
def motor2(value):
    if value < 0 and value >= -100:
        motor3r = 0
        motor3l = 1
        motor3speed = abs(value)
        print('Motor3 is rotating CCW')
    if value > 0 and value <= 100:
        motor3r = 1
        motor3l = 0
        motor3speed = abs(value)
        print('Motor3 is rotating CW')
    if value == 0:
        motor3r = 0
        motor3l = 0
        motor3speed = 0
        print('Motor3 is not rotating')
    if value < -100 or value > 100:
        print('error')
        # come back and do changes here
    en03.ChangeDutyCycle(motor3speed)
    GPIO.output(MOTOR3L, motor3l)
    GPIO.output(MOTOR3R, motor3r)


# Determine the velocities of the motors based on the given heading_angle and velocity, and rotational velocity
def move(DesiredDirection, velocity, rotation):  # velocity from 0 to 80 rotation -20 to 20

##    DesiredDirection = -DesiredDirection
    
    Fa = -(velocity * dcos(150 - DesiredDirection) + rotation)  # motor 1
    Fb = -(velocity * dcos(30 - DesiredDirection) + rotation)  # motor 2
    Fc = -(velocity * dcos(270 - DesiredDirection) + rotation)  # motor 3

    if Fa>100 or Fb>100 or Fc>100:
        maxx= max(Fa,Fb,Fc)
        Fa=Fa*100/maxx
        Fb=Fb*100/maxx
        Fc=Fc*100/maxx
        
    print('Motor 1 Speed is', round(Fc))
    print('Motor 2 Speed is', round(Fa))
    print('Motor 3 Speed is', round(Fb))
    motor1(round(Fc))
    motor2(round(Fa))
    motor3(round(Fb))

def stops():
    GPIO.output(MOTOR1L, 0)
    GPIO.output(MOTOR1R, 0)

    GPIO.output(MOTOR2L, 0)
    GPIO.output(MOTOR2R, 0)

    GPIO.output(MOTOR3L, 0)
    GPIO.output(MOTOR3R, 0)
    
    

##move(0, 80, 0)
##move(-25, 35, 3.5)
move(25, 35, 3.5)

