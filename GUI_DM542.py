import sys
from DM542 import StepDriver
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QGridLayout,
                             QPushButton, QApplication, QInputDialog,
                             QLineEdit, QComboBox, QLabel)

class StepController(QWidget):
    def __init__(self):
        super().__init__()
        self.drv = StepDriver()
        self.initUI()
    
    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        self.lcd_position = QLCDNumber(self)
        grid.addWidget(self.lcd_position, 0, 3)

        button_counterclockwise_step = QPushButton("Counterclockwise")
        grid.addWidget(button_counterclockwise_step, 1, 0)
        button_counterclockwise_step.clicked.connect(self.step_counterlockwise)

        button_clear = QPushButton("Clear")
        grid.addWidget(button_clear, 3, 0)
        button_clear.clicked.connect(self.event_on_button_clear)

        button_clockwise_step = QPushButton("Clockwise")
        grid.addWidget(button_clockwise_step, 2, 0)
        button_clockwise_step.clicked.connect(self.step_clockwise)
        
        self.settings_label = QLabel("Settings")
        grid.addWidget(self.settings_label, 1, 2)
        
        self.delay_label = QLabel("Step's delay")
        grid.addWidget(self.delay_label, 2, 2)
        
        self.delay_Eline = QLineEdit(f"Actual ammount of steps per loop is: {self.drv.delay_sec}")
        self.delay_Eline.returnPressed.connect(self.set_delay)
        grid.addWidget(self.delay_Eline, 2, 3)
        
        self.steps_label = QLabel("Step's number")
        grid.addWidget(self.steps_label, 3, 2)
        
        self.steps_Eline = QLineEdit(f"Actual ammount of steps per loop is: {self.drv.steps}")
        self.steps_Eline.returnPressed.connect(self.set_steps_number)
        grid.addWidget(self.steps_Eline, 3, 3)
        
        self.setGeometry(300, 300, 700, 320)
        self.setWindowTitle("Stepmotor")
        self.show()
    
    def set_steps_number(self):
        text = self.steps_Eline.text()
        try:
            steps = int(text)
            self.drv.steps = steps
            self.steps_Eline.setText(f"Actual ammount of steps per loop is: {text}")
        except:
            self.steps_Eline.setText("input musst be of the type integer")
    
    def set_delay(self):
        text = self.delay_Eline.text()
        try:
            delay = float(text)
            self.drv.delay_sec = delay
            self.delay_Eline.setText(f"Actual delay between steps is: {text}")
        except:
            self.delay_Eline.setText(f"input musst be of the type float")    

    def step_clockwise(self):
        self.lcd_position.display(self.lcd_position.intValue() + 1)
        self.drv.clockwise_step()               
    
    def step_counterlockwise(self):
        self.lcd_position.display(self.lcd_position.intValue() - 1)
        self.drv.counterclockwise_step()

    def event_on_button_clear(self):        
        self.lcd_position.display(0)         

def main():
    app =  QApplication(sys.argv)
    controller = StepController()
    sys.exit(app.exec_())
    GPIO.clearup()

if __name__ == "__main__":
     main()