import sys
from DRV8825 import StepDriver
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
        grid.addWidget(self.lcd_position, 0, 1)

        button_counterclockwise_step = QPushButton("Counterclockwise")
        grid.addWidget(button_counterclockwise_step, 1, 0)
        button_counterclockwise_step.clicked.connect(self.step_counterlockwise)

        button_stop = QPushButton("Stop")
        grid.addWidget(button_stop, 3, 0)
        button_stop.clicked.connect(self.event_on_button_stop)

        button_clockwise_step = QPushButton("Clockwise")
        grid.addWidget(button_clockwise_step, 2, 0)
        button_clockwise_step.clicked.connect(self.step_clockwise)
        
        self.settings_label = QLabel("Settings")
        grid.addWidget(self.settings_label, 1, 2)
        
        self.step_size_label = QLabel("Step size:")
        grid.addWidget(self.step_size_label, 2, 2)
        
        self.steps_label = QLabel("Step's number")
        grid.addWidget(self.steps_label, 3, 2)
        
        self.steps_Eline = QLineEdit("set number of steps")
        self.steps_Eline.returnPressed.connect(self.set_steps_number)
        grid.addWidget(self.steps_Eline, 3, 3)
        
        self.steps_box = QComboBox(self)
        for item in self.drv.RESOLUTION:
            self.steps_box.addItem(item)
        self.steps_box.activated[str].connect(self.set_step_size)
        grid.addWidget(self.steps_box, 2, 3)
        
        self.setGeometry(300, 300, 600, 320)
        self.setWindowTitle("Stepmotor")
        self.show()
        
    def set_step_size(self):
        text = self.steps_box.currentText()
        self.drv.set_resolution(text)
    
    def set_steps_number(self):
        text = self.steps_Eline.text()
        try:
            steps = int(text)
            self.drv.steps = steps
            self.steps_Eline.setText(f"spes number is {text}")
        except:
            self.steps_Eline.setText("input musst be integer")           

    def step_clockwise(self):
        self.lcd_position.display(self.lcd_position.intValue() + 1)
        self.drv.counterclockwise_step()               
    
    def step_counterlockwise(self):
        self.lcd_position.display(self.lcd_position.intValue() - 1)
        self.drv.counterclockwise_step()

    def event_on_button_stop(self):        
        self.lcd_position.display(0)         

def main():
    app =  QApplication(sys.argv)
    controller = StepController()
    sys.exit(app.exec_())    

if __name__ == "__main__":
     main()