import sys # this module provides variables used to maintain python interpreter
#well also need widgets are the building blocks of a gui application
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout)
#Qtcore provide functionalities not related to gui components
from PyQt5.QtCore import QTimer, QTime, Qt

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()

        #start designing the stopwatch
        self.time = QTime(0,0,0,0)
        self.time_label = QLabel('00:00:00:00', self)
        self.start_button = QPushButton('Start', self)
        self.stop_button = QPushButton('Stop', self)
        self.reset_button = QPushButton('Reset', self)
        self.timer = QTimer(self)

        self.initUI()#but I still have to define this method

    def initUI(self):
        self.setWindowTitle('StopWatch')

        vbox = QVBoxLayout()
        #ill take the layout manager and add the following widgets
        vbox.addWidget(self.time_label)


        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
           QPushButton{
              font-size: 50px;
           }
           QLabel{
              font-size: 120px;
              background-color: hsl(300, 98%, 49%);
           }
        
        """)

        #now connecting the signal to the slot for the buttons to function

        self.start_button.clicked.connect(self.start) # type: ignore
        self.stop_button.clicked.connect(self.stop) # type: ignore
        self.reset_button.clicked.connect(self.reset) # type: ignore
        self.timer.timeout.connect(self.update_display) # type: ignore


    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    #@staticmethod
    def format_time(self, time):
        hours = time.hour()
        minutes = time.minutes()
        seconds = time.seconds()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10) #im updating time with + 10 milliseconds
        self.time_label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_()) #this executes method starts the main event loop and handles events