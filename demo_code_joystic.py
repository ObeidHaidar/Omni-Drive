from math import cos,pi,radians
import time
import RPi.GPIO as GPIO

MOTOR1L = 20
MOTOR1R = 21
MOTOR1PWM = 16

MOTOR2L = 26
MOTOR2R = 19
MOTOR2PWM = 13

MOTOR3R = 5
MOTOR3L = 6
MOTOR3PWM = 12

MOTORPWMFREQUENCY = 50 # IN Hz



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(MOTOR1L,GPIO.OUT)
GPIO.setup(MOTOR1R,GPIO.OUT)
GPIO.setup(MOTOR1PWM,GPIO.OUT)
GPIO.setup(MOTOR2L,GPIO.OUT)
GPIO.setup(MOTOR2R,GPIO.OUT)
GPIO.setup(MOTOR2PWM,GPIO.OUT)
GPIO.setup(MOTOR3L,GPIO.OUT)
GPIO.setup(MOTOR3R,GPIO.OUT)
GPIO.setup(MOTOR3PWM,GPIO.OUT)

en01 = GPIO.PWM(MOTOR1PWM,MOTORPWMFREQUENCY)
en01.start(0)
en02 = GPIO.PWM(MOTOR2PWM,MOTORPWMFREQUENCY)
en02.start(0)
en03 = GPIO.PWM(MOTOR3PWM,MOTORPWMFREQUENCY)
en03.start(0)


def dcos(a):
    return cos(radians(a))

def motor1(value):
    if value<0 and value >=-100:
        motor1r = 0
        motor1l = 1
        motor1speed = abs(value)
        print('Motor1 is rotating CCW')
    elif value>0 and value<=100:
        motor1r = 1
        motor1l = 0
        motor1speed = abs(value)
        print('Motor1 is rotating CW')
    elif value == 0:
        motor1r = 0
        motor1l = 0
        motor1speed = 0
        print('Motor1 is not rotating')
    elif value<-100 or value>100:
        print('error')
        #come back and do changes here
    en01.ChangeDutyCycle(motor1speed)
    GPIO.output(MOTOR1L,motor1l)
    GPIO.output(MOTOR1R,motor1r)


def motor3(value):
    if value<0 and value >=-100:
        motor2r = 0
        motor2l = 1
        motor2speed = abs(value)
        print('Motor2 is rotating CCW')
    if value>0 and value <=100:
        motor2r = 1
        motor2l = 0
        motor2speed = abs(value)
        print('Motor2 is rotating CW')
    if value == 0:
        motor2r = 0
        motor2l = 0
        motor2speed = 0
        print('Motor2 is not rotating')
    if value<-100 or value>100:
        print('error')
        #come back and do changes here
    en02.ChangeDutyCycle(motor2speed)
    GPIO.output(MOTOR2L,motor2l)
    GPIO.output(MOTOR2R,motor2r)

def motor2(value):
    if value<0 and value >=-100:
        motor3r = 0
        motor3l = 1
        motor3speed = abs(value)
        print('Motor3 is rotating CCW')
    if value>0 and value <=100:
        motor3r = 1
        motor3l = 0
        motor3speed = abs(value)
        print('Motor3 is rotating CW')
    if value == 0:
        motor3r = 0
        motor3l = 0
        motor3speed = 0
        print('Motor3 is not rotating')
    if value<-100 or value>100:
        print('error')
        #come back and do changes here
    en03.ChangeDutyCycle(motor3speed)
    GPIO.output(MOTOR3L,motor3l)
    GPIO.output(MOTOR3R,motor3r)
        

def move(DesiredDirection,velocity,rotation): #velocity from 0 to 80 rotation -20 to 20
    Fa = velocity*dcos(150 - DesiredDirection)+rotation #motor 1
    Fb = velocity*dcos(30  - DesiredDirection)+rotation #motor 2
    Fc = velocity*dcos(270 - DesiredDirection)+rotation #motor 3
    print('Motor 1 Speed is',round(Fa))
    print('Motor 2 Speed is',round(Fb))
    print('Motor 3 Speed is',round(Fc)) 
    motor1(round(Fa))
    motor2(round(Fb))
    motor3(round(Fc))
    return

import pygame

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    

pygame.init()
 
# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
    
# Get ready to print
textPrint = TextPrint()
angle=0
rotation=0
velocity=0
start_button=0

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
            
 
    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    textPrint.print(screen, "Number of joysticks: {}".format(joystick_count) )
    textPrint.indent()
    
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
        textPrint.print(screen, "Joystick {}".format(i) )
        textPrint.indent()
    
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        textPrint.print(screen, "Joystick name: {}".format(name) )
        
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        textPrint.print(screen, "Number of axes: {}".format(axes) )
        textPrint.indent()
        
        for i in range( axes ):
            axis = joystick.get_axis( i )
            textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
        textPrint.unindent()
        # rotation for motor is controlled by the left analog
        if start_button==1:          
            rotation= 20*joystick.get_axis( 0 )
            velocity = 56*sqrt(((joystick.get_axis( 3 ))**2) + ((joystick.get_axis( 4 ))**2))
            if joystick.get_axis(4)==-1 and joystick.get_axis(3)==0:
                angle=0
            if joystick.get_axis(4)==1 and joystick.get_axis(3)==0:
                angle=180
            if joystick.get_axis(4)==0 and joystick.get_axis(3)==0:
                angle=0
            if joystick.get_axis(4)==0 and joystick.get_axis(3)==1:
                angle=270
            if joystick.get_axis(4)==0 and joystick.get_axis(3)==-1:
                angle=90
            if joystick.get_axis(4)<0 and joystick.get_axis(3)<0:
                angle=0 + datan(abs(joystick.get_axis(3))/abs(joystick.get_axis(4)))
            if joystick.get_axis(4)>0 and joystick.get_axis(3)<0:
                angle=90 + datan(abs(joystick.get_axis(3))/abs(joystick.get_axis(4)))
            if joystick.get_axis(4)>0 and joystick.get_axis(3)>0:
                angle=180 + datan(abs(joystick.get_axis(3))/abs(joystick.get_axis(4)))
            if joystick.get_axis(4)<0 and joystick.get_axis(3)>0:
                angle=270 + datan(abs(joystick.get_axis(3))/abs(joystick.get_axis(4)))
            if joystick.get_axis( 5 ) > -0.95:
                velocity = 40*(joystick.get_axis( 5 )+1)
                angle=0
            if joystick.get_axis( 2 ) > -0.95:
                velocity = 40*(joystick.get_axis( 5 )+1)
                angle=180
        buttons = joystick.get_numbuttons()
        textPrint.print(screen, "Number of buttons: {}".format(buttons) )
        textPrint.indent()

        for i in range( buttons ):
            button = joystick.get_button( i )
            textPrint.print(screen, "Button {:>2} value: {}".format(i,button) )
        textPrint.unindent()
        if joystick.get_button( 7 )==1:
            start_button=1   
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        textPrint.print(screen, "Number of hats: {}".format(hats) )
        textPrint.indent()

        for i in range( hats ):
            hat = joystick.get_hat( i )
            textPrint.print(screen, "Hat {} value: {}".format(i, str(hat)) )
        textPrint.unindent()
        
        textPrint.unindent()

    
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    move(angle,velocity,rotation)
    # Limit to 20 frames per second
    clock.tick(10)
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
