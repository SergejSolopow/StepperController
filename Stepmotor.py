from time import sleep
from RPi import GPIO

class StepDriver:
    
    def __init__(self, direction = 20, step = 21):
        
        self.delay_sec= 0.02 #delay_sec used for sleep event in methods used below
        self.direction = direction #self is a numer of tteh pin on the RPi board responsible for the roation's direction 
        self.step = step #self is a number of the pin on the RPi board responsible for teh one step event  
        self.is_run = True
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM) #define number specification on the RPi board
        GPIO.setup(direction, GPIO.OUT) #setup of the direction pin
        GPIO.setup(step, GPIO.OUT) #setup of teh step-event pin
    
    def clockwise_step(self):
        GPIO.output(self.direction, 1)
        sleep(0.005)        
        GPIO.output(self.step, GPIO.HIGH)
        sleep(self.delay_sec)
        GPIO.output(self.step, GPIO.LOW)
        
    
    def counterclockwise_step(self):
        GPIO.output(self.direction, 0)
        sleep(0.005)
        GPIO.output(self.step, GPIO.HIGH)
        sleep(self.delay_sec)
        GPIO.output(self.step, GPIO.LOW)
    
    def run_clocwise(self):
        GPIO.output(self.direction, 1)
        sleep(0.005)
        while self.is_run:
            GPIO.output(self.step, GPIO.HIGH)
            sleep(self.delay_sec)
            GPIO.output(self.step, GPIO.LOW)
            sleep(self.delay_sec)
    
    def stop_run(self):
        self.is_run = False
        
        
        