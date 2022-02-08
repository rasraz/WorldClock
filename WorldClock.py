from PyQt5 import QtWidgets,QtCore,QtGui
from datetime import datetime
import sys
import time
import pytz

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.UiApp()
        self.show()
    
    def UiApp(self):
        self.setGeometry(100,100,750, 390)
        self.setWindowTitle('World Clock')


        self.list_clock={}

        LineEdit_timezone=QtWidgets.QLineEdit(self)
        complater=QtWidgets.QCompleter(pytz.all_timezones)
        LineEdit_timezone.setCompleter(complater)
        LineEdit_timezone.setToolTip("Write timezone")
        LineEdit_timezone.move(600,20)
        button_addTimeZone=QtWidgets.QPushButton('Add New Clock',self)
        button_addTimeZone.move(615,60)
        
        self.frame=QtWidgets.QWidget(self)

        button_addTimeZone.clicked.connect(lambda:self.addNewClock(LineEdit_timezone.text()))
        
        self.VBoxLayout=QtWidgets.QVBoxLayout()

        self.addNewClock('CurrentLocation')

        self.frame.setLayout(self.VBoxLayout)
        
        self.scroll = QtWidgets.QScrollArea(self)
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.frame)
        self.scroll.setGeometry(0,10,600, 380)

        timer=QtCore.QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        
    def showtime(self):
        for i in self.list_clock:
            if i=='CurrentLocation':
                now_time = time.localtime()
                str_clock = time.strftime("%H:%M:%S", now_time)
                self.list_clock[i][1].setText('Current\nLocation')
                self.list_clock[i][2].setText(str_clock)
            else:
                print(datetime.now())
                UTC = pytz.utc
                timeZ = pytz.timezone(i)
                dt = datetime.now(timeZ)
                self.list_clock[i][1].setText(i)
                self.list_clock[i][2].setText(dt.strftime('%H:%M:%S'))

    
    def addNewClock(self,TimeZone):
        grid=QtWidgets.QGridLayout()

        label_location=QtWidgets.QLabel('Hello')
        label_location.setStyleSheet('background-color:green;border-radius:10px;')
        label_location.setAlignment(QtCore.Qt.AlignCenter)
        font_location = QtGui.QFont('Arial',20,QtGui.QFont.Bold)
        label_location.setFont(font_location)
        grid.addWidget(label_location,0,0,0,2)

        label_time=QtWidgets.QLabel('Worled')
        label_time.setStyleSheet('background-color:red;border-radius:10px;')
        label_time.setAlignment(QtCore.Qt.AlignCenter)
        font_time = QtGui.QFont('Arial',70,QtGui.QFont.Bold)
        label_time.setFont(font_time)
        grid.addWidget(label_time,0,2,0,6)
        
        self.list_clock[TimeZone]=[grid,label_location,label_time]

        self.frame.setGeometry(0,10,600,self.frame.frameGeometry().height()+120)
        self.VBoxLayout.addLayout(grid)
        

if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    win=Window()
    sys.exit(app.exec_())

