from RPi import GPIO
import psutil
from time import sleep

class TepmeratureSensor:
    
    def __init__(self, delay = 0.2):
        self.cpu = psutil.cpu_percent()
        self.delay = delay
        self.run_sensor = True
    
    def get_temperature(self, delay):
        while self.run_sensor:
            self.cpu = psutil.cpu_percent()
            print(self.cpu)
            sleep(self.delay)    
    