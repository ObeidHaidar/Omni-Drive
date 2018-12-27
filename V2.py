from math import cos,pi,radians
import time

def dcos(a):
    return cos(radians(a))

def motor1(value):
    if value<0 and value >=-255:
        motor1r = 0
        motor1l = 1
        motor1speed = abs(value)
        print('Motor1 is rotating CCW')
    elif value>0 and value<=255:
        motor1r = 1
        motor1l = 0
        motor1speed = abs(value)
        print('Motor1 is rotating CW')
    elif value == 0:
        motor1r = 0
        motor1l = 0
        motor1speed = 0
        print('Motor1 is not rotating')
    elif value<-255 or value>255:
        print('error')
        #come back and do changes here

def motor2(value):
    if value<0 and value >=-255:
        motor2r = 0
        motor2l = 1
        motor2speed = abs(value)
        print('Motor2 is rotating CCW')
    if value>0 and value <=255:
        motor2r = 1
        motor2l = 0
        motor2speed = abs(value)
        print('Motor2 is rotating CW')
    if value == 0:
        motor2r = 0
        motor2l = 0
        motor2speed = 0
        print('Motor2 is not rotating')
    if value<-255 or value>255:
        print('error')
        #come back and do changes here

def motor3(value):
    if value<0 and value >=-255:
        motor3r = 0
        motor3l = 1
        motor3speed = abs(value)
        print('Motor3 is rotating CCW')
    if value>0 and value <=255:
        motor3r = 1
        motor3l = 0
        motor3speed = abs(value)
        print('Motor3 is rotating CW')
    if value == 0:
        motor3r = 0
        motor3l = 0
        motor3speed = 0
        print('Motor3 is not rotating')
    if value<-255 or value>255:
        print('error')
        #come back and do changes here
def move(DesiredDirection,velocity): #velocity from 0 to 255
    Fa = velocity*dcos(150 - DesiredDirection) #motor 1
    Fb = velocity*dcos(30  - DesiredDirection) #motor 2
    Fc = velocity*dcos(270 - DesiredDirection) #motor 3
    print('Motor 1 Speed is',round(Fa))
    print('Motor 2 Speed is',round(Fb))
    print('Motor 3 Speed is',round(Fc)) 
    motor1(round(Fa))
    motor2(round(Fb))
    motor3(round(Fc))
    return
def turn(DesiredAngle,velocity):
    R
