import sys
from PyQt5.QtWidgets import (QWidget, QLCDNumber,
QGridLayout, QPushButton, QApplication)

class StepController(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        self.lcd_position = QLCDNumber(self)
        grid.addWidget(self.lcd_position, 0, 1)

        button_left = QPushButton("Left")
        grid.addWidget(button_left, 1, 0)
        button_left.clicked.connect(self.event_on_button_left)

        button_stop = QPushButton("Stop")
        grid.addWidget(button_stop, 1, 1)
        button_stop.clicked.connect(self.event_on_button_stop)

        button_right = QPushButton("Right")
        grid.addWidget(button_right, 1, 2)
        button_right.clicked.connect(self.event_on_button_right)

        self.setGeometry(300, 300, 600, 320)
        self.setWindowTitle("Stepmotor")
        self.show()

    def event_on_button_right(self):
        self.lcd_position.display(self.lcd_position.intValue() + 1)        
    
    def event_on_button_left(self):
        self.lcd_position.display(self.lcd_position.intValue() - 1)


    def event_on_button_stop(self):        
        self.lcd_position.display(0)
           

def main():
    app =  QApplication(sys.argv)
    controller = StepController()
    sys.exit(app.exec_())

if __name__ == "__main__":
     main()