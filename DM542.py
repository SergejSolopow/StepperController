from time import sleep
from RPi import GPIO

#Code is wreeten for the control of stepper driver DRV8825 with RPi 
class StepDriver:    
    def __init__(self, DIR = 33, PUL = 35, ENA = 37):        
        self.delay_sec= 0.005 #delay_sec used for sleep event in methods used below
        self.ENA = ENA #set pin's number for enable/desable the motor
        self.DIR = DIR #pin number on the RPi board responsible for the roation's direction 
        self.PUL = PUL #pin number on the RPi board responsible for the one step event
        self.steps = 1 #how many steps getting executed over one event
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD) #define enumiration specification on the RPi board               
        GPIO.setup(DIR, GPIO.OUT) #setup the direction pin
        GPIO.setup(PUL, GPIO.OUT) #setup the step-event pin
        GPIO.setup(ENA, GPIO.OUT)
    
    def clockwise_step(self):
        GPIO.output(self.ENA, GPIO.LOW) #activate and hold the motor
        GPIO.output(self.DIR, GPIO.HIGH) #define rotation's direction
        for x in range(self.steps): #set HIGH and LOW signal to the PUL to variate curent on the cooils
            GPIO.output(self.PUL, GPIO.HIGH)
            sleep(self.delay_sec)
            GPIO.output(self.PUL, GPIO.LOW)
            sleep(self.delay_sec)
        GPIO.output(self.ENA, GPIO.HIGH) #deactivate the motor
    
    def counterclockwise_step(self):
        GPIO.output(self.ENA, GPIO.LOW)
        GPIO.output(self.DIR, GPIO.LOW)
        for x in range(self.steps):
            GPIO.output(self.PUL, GPIO.HIGH)
            sleep(self.delay_sec)
            GPIO.output(self.PUL, GPIO.LOW)
            sleep(self.delay_sec)
        GPIO.output(self.ENA, GPIO.HIGH)   