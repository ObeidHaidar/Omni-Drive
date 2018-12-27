import math

#EGB320 Code V.01
def motor1(status,PWM):
    if status == 'cw':
        print('Motor1 is rotating CW')
        motor1r = 1
        motor1l = 0
        motor1PWM = PWM
    elif status == 'ccw':
        print('Motor1 is rotating CCW')
        motor1r = 0
        motor1l = 1
        motor1PWM = PWM
    elif status == 'stop':
        print('Motor1 stopped')
        motor1r = 0
        motor1l = 0
    elif status == 'break':
        print('Motor1 breaked')
        motor1r = 1
        motor1l = 1        
    else :
        print('ERROR choose between cw and ccw')
    return

def motor2(status,PWM):
    if status == 'cw':
        print('Motor2 is rotating CW')
        motor2r = 1
        motor2l = 0
        motor2PWM = PWM
    elif status == 'ccw':
        print('Motor2 is rotating CCW')
        motor2r = 0
        motor2l = 1
        motor2PWM = PWM
    elif status == 'stop':
        print('Motor2 stopped')
        motor2r = 0
        motor2l = 0
    elif status == 'break':
        print('Motor2 breaked')
        motor2r = 1
        motor2l = 1        
    else :
        print('ERROR choose between cw and ccw')
    return

def motor3(status,PWM):
    if status == 'cw':
        print('Motor3 is rotating CW')
        motor3r = 1
        motor3l = 0
        motor3PWM = PWM
    elif status == 'ccw':
        print('Motor3 is rotating CCW')
        motor3r = 0
        motor3l = 1
        motor3PWM = PWM
    elif status == 'stop':
        print('Motor3 stopped')
        motor3r = 0
        motor3l = 0
    elif status == 'break':
        print('Motor3 breaked')
        motor3r = 1
        motor3l = 1        
    else :
        print('ERROR choose between cw and ccw')
    return
def motor(DesiredDirection,velocity): #velocity from 0 to 255
    Fa = velocity*math.cos((150 - DesiredDirection)/(180/math.pi)) #motor 1
    Fb = velocity*math.cos((30 - DesiredDirection)/(180/math.pi)) #motor 2
    Fc = velocity*math.cos((270 - DesiredDirection)/(180/math.pi)) #motor 3
    print('Motor 1 Speed is',round(Fa))
    print('Motor 2 Speed is',round(Fb))
    print('Motor 3 Speed is',round(Fc)) 
    if Fa>0:
        motor1('cw',abs(Fa))
    elif Fa<0:
        motor1('ccw',abs(Fa))
    elif Fa == 0:
        motor1('stop')

    if Fb>0:
        motor2('cw',abs(Fb))
    elif Fb<0:
        motor2('ccw',abs(Fb))
    elif Fb == 0:
        motor2('stop')
    
    if Fc>0:
        motor3('cw',abs(Fc))
    elif Fc<0:
        motor3('ccw',abs(Fc))
    elif Fc == 0:
        motor3('stop')
    return
#def rotate(angle,speed):
    
