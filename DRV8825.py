from time import sleep
from RPi import GPIO

#Code is wreeten for the control of stepper driver DRV8825 with RPi 
class StepDriver:    
    def __init__(self, direction = 20, step = 21, resolution = "1/32"):        
        self.delay_sec= 0.001 #delay_sec used for sleep event in methods used below
        self.direction = direction #pin number on the RPi board responsible for the roation's direction 
        self.step = step #pin number on the RPi board responsible for the one step event
        self.steps = 1 #how many steps getting executed over one event
        self.is_run = True         
        GPIO.setmode(GPIO.BCM) #define number specification on the RPi board
        self.MODE = (14, 15, 16) #pinout's numbers on RPi board to manage the step-size
        self.RESOLUTION = { "Full" : (0, 0, 0),
                       "Half" : (0, 1, 0),
                       "1/4" : (0, 1, 0),
                       "1/8" : (0, 1, 0),
                       "1/16" : (0, 1, 0),
                       "1/32" : (0, 1, 0)}
        GPIO.setwarnings(False)
        GPIO.setup(self.MODE, GPIO.OUT) #setup pinouts fro defined resolution
        GPIO.output(self.MODE, self.RESOLUTION[resolution])        
        GPIO.setup(direction, GPIO.OUT) #setup of the direction pin
        GPIO.setup(step, GPIO.OUT) #setup of teh step-event pin
    
    def set_resolution(self, resolution):
        GPIO.output(self.MODE, self.RESOLUTION[resolution])        
    
    def clockwise_step(self):
        GPIO.output(self.direction, 1)
        sleep(0.005)
        for x in range(self.steps):
            GPIO.output(self.step, GPIO.HIGH)
            sleep(self.delay_sec)
            GPIO.output(self.step, GPIO.LOW)
            sleep(self.delay_sec)        
    
    def counterclockwise_step(self):
        GPIO.output(self.direction, 0)
        sleep(0.005)
        for x in range(self.steps):
            GPIO.output(self.step, GPIO.HIGH)
            sleep(self.delay_sec)
            GPIO.output(self.step, GPIO.LOW)
            sleep(self.delay_sec)
    
    def stop_run(self):
        self.is_run = False