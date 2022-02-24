from TemperatureSensor import TepmeratureSensor
from Stepmotor import StepDriver

class TemperatureControlling:
    def __init__(self):
        self.motor = StepDriver()
        self.temperature = TepmeratureSensor()

if __name__ == "__main__":
    controller = TemperatureControlling()
