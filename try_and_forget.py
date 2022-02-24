import psutil
from time import sleep
from multiprocessing import Process
from threading import Thread
import multiprocessing

class DigitTemperature:
    
    def __init__(self):
        self.cpu = 0
        self.run_temperature = True
    
    def cpu_value(self):
        while self.run_temperature:
            self.cpu = psutil.cpu_percent()
            sleep(1.5)

class Motor:
    
    def __init__(self):
        self.run_motor = True
        self.instance_temperature = DigitTemperature()
        self.th1 = Thread(target = self.instance_temperature.cpu_value)
        self.th2 = Thread(target = self.response_motor)
        self.th1.start()
        self.th2.start()
        self.th1.join()
        self.th2.join()
        
    def response_motor(self):
        while self.run_motor:
            if self.instance_temperature.cpu < 10:
                print("Green")
            elif self.instance_temperature.cpu >70:
                print("Red")
            else:
                print("Yelow")
            sleep(2)


if __name__ == '__main__':
    motor = Motor()
    
    
    