import sys
from Stepmotor import StepDriver
from PyQt5.QtWidgets import (QWidget, QLCDNumber,
QGridLayout, QPushButton, QApplication)

class StepController(QWidget):
    def __init__(self):
        super().__init__()
        self.drv = StepDriver()
        self.initUI()
    
    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        self.lcd_position = QLCDNumber(self)
        grid.addWidget(self.lcd_position, 0, 1)

        button_counterclockwise_step = QPushButton("Counterclockwise")
        grid.addWidget(button_counterclockwise_step, 1, 0)
        button_counterclockwise_step.clicked.connect(self.step_counterlockwise)

        button_stop = QPushButton("Stop")
        grid.addWidget(button_stop, 1, 1)
        button_stop.clicked.connect(self.event_on_button_stop)

        button_clockwise_step = QPushButton("Clockwise")
        grid.addWidget(button_clockwise_step, 1, 2)
        button_clockwise_step.clicked.connect(self.step_clockwise)
        
        button_clockwise_run = QPushButton("Clockwise run")
        grid.addWidget(button_clockwise_run, 2, 2)
        button_clockwise_run.clicked.connect(self.run_clockwise)
        

        self.setGeometry(300, 300, 600, 320)
        self.setWindowTitle("Stepmotor")
        self.show()

    def step_clockwise(self):
        self.lcd_position.display(self.lcd_position.intValue() + 1)
        self.drv.clockwise_step()
        
    
    def step_counterlockwise(self):
        self.lcd_position.display(self.lcd_position.intValue() - 1)
        self.drv.counterclockwise_step()


    def event_on_button_stop(self):        
        self.lcd_position.display(0)
    
    def run_clockwise(self):
        self.drv.run_clocwise()
        
           

def main():
    app =  QApplication(sys.argv)
    controller = StepController()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
     main()