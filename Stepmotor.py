from time import sleep
from RPi import GPIO

class StepDriver:
    
    def __init__(self, direction = 20, step = 21, resolution = "1/32"):
        
        self.delay_sec= 0.02 #delay_sec used for sleep event in methods used below
        self.direction = direction #self is a numer of tteh pin on the RPi board responsible for the roation's direction 
        self.step = step #self is a number of the pin on the RPi board responsible for teh one step event  
        self.is_run = True
        GPIO.setmode(GPIO.BCM) #define number specification on the RPi board
        MODE = (14, 15, 16) #pinout's numbers on RPi board to manage the step-size
        RESOLUTION = { "Full" : (0, 0, 0),
                       "Half" : (0, 1, 0),
                       "1/4" : (0, 1, 0),
                       "1/8" : (0, 1, 0),
                       "1/16" : (0, 1, 0),
                       "1/32" : (0, 1, 0)}
        GPIO.setwarnings(False)
        GPIO.setup(MODE, GPIO.OUT) #setup pinouts fro defined resolution
        GPIO.output(MODE, RESOLUTION[resolution])        
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