from PyQt5 import QtWidgets,QtCore,QtGui
import sys
import time 

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.UiApp()
        self.show()
    
    def UiApp(self):
        self.setGeometry(100,100,600, 120)

        grid=QtWidgets.QGridLayout()


        self.label_location=QtWidgets.QLabel('Hello')
        self.label_location.setStyleSheet('background-color:green;')
        self.label_location.setAlignment(QtCore.Qt.AlignCenter)
        font_location = QtGui.QFont('Arial',30,QtGui.QFont.Bold)
        self.label_location.setFont(font_location)
        grid.addWidget(self.label_location,0,0,0,2)

        self.label_time=QtWidgets.QLabel('Worled')
        self.label_time.setStyleSheet('background-color:red;')
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        font_time = QtGui.QFont('Arial',70,QtGui.QFont.Bold)
        self.label_time.setFont(font_time)
        grid.addWidget(self.label_time,0,2,0,6)

        VBoxLayout=QtWidgets.QVBoxLayout()
        VBoxLayout.addLayout(grid)
        self.setLayout(VBoxLayout)

        timer=QtCore.QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)

    def showtime(self):
        now_time = time.localtime()
        str_clock = time.strftime("%H:%M:%S", now_time)
        self.label_location.setText('Current location')
        self.label_time.setText(str_clock)
        

if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    win=Window()
    sys.exit(app.exec_())

