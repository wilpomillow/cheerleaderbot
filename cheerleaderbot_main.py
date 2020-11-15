import os
from random import randint
from playsound import playsound
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import pyautogui, sys, time
from time import time, sleep
from datetime import datetime, timedelta

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100,200,80,240)
        self.setWindowTitle('Procrastionation Police')
        self.setWindowIcon(QtGui.QIcon('procrast_ico.png'))
        self.initUI()
    
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('Focus!')
        self.label.move(5,0)

        self.radiobutton1 = QRadioButton(self)
        self.radiobutton1.setText("English (EN)")
        self.radiobutton1.language = "EN"
        self.radiobutton1.move(5,45)
        self.radiobutton1.setChecked(True)
        self.radiobutton1.toggled.connect(self.onClicked)
        self.radiobutton1.adjustSize()
        
        self.radiobutton2 = QRadioButton(self)
        self.radiobutton2.setText("Chinese (CN)")
        self.radiobutton2.language = "CN"
        self.radiobutton2.move(5,70)
        self.radiobutton2.toggled.connect(self.onClicked)
        self.radiobutton2.adjustSize()

        self.radiobutton3 = QRadioButton(self)
        self.radiobutton3.setText("Chinese (SH)")
        self.radiobutton3.language = "SH"
        self.radiobutton3.move(5,95)
        self.radiobutton3.toggled.connect(self.onClicked)
        self.radiobutton3.adjustSize()

        self.radiobutton4 = QRadioButton(self)
        self.radiobutton4.setText("Japanese (JP)")
        self.radiobutton4.language = "JP"
        self.radiobutton4.move(5,120)
        self.radiobutton4.toggled.connect(self.onClicked)
        self.radiobutton4.adjustSize()

        self.radiobutton5 = QRadioButton(self)
        self.radiobutton5.setText("English (UWU)")
        self.radiobutton5.language = "UWU"
        self.radiobutton5.move(5,145)
        self.radiobutton5.toggled.connect(self.onClicked)
        self.radiobutton5.adjustSize()

        self.b1 = QPushButton(self)
        self.b1.setText('Select')
        self.b1.move(5,200)
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText('Focusing')
        self.update()
        languagefolder = language_sel
        list = os.listdir(dir+'\\'+languagefolder)
        number_files = len(list)
        print('Number of files: ', number_files)

        second_count = 1
        nowtime = time()
        
        naughty_counter = 0

        try:
            while naughty_counter < 9000:
                
                # Track the mouse
                x, y = pyautogui.position()
                positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

                # Track the time
                second_count+=1

                    # Reset if the mouse moves
                x1, y1 = pyautogui.position()
                if x1 != x and y1 != y:
                    print('\n','Moved after:',time_spent)
                    nowtime = time()

                sec = timedelta(seconds=int(time()-nowtime))
                d = datetime(1,1,1)+sec
                time_spent = str("%d:%d:%d:%d" % (d.day-1, d.hour, d.minute, d.second))

                # Output
                together_str = str(positionStr+ '  Timer: '+ time_spent)
                print(together_str, end='')
                print('\b' * len(together_str), end='', flush=True)

                if  d.second == 20:
                    random_index = str(randint(1,number_files))
                    print('Playing:'+random_index+'.wav')
                    playsound(str((dir+'\\'+languagefolder+'\\'+random_index+'.wav')))
                    nowtime = time()
                    naughty_counter += 1

        
        except KeyboardInterrupt:
            print('\n')
    
    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print("language is %s" % (radioButton.language))
            global language_sel
            language_sel = radioButton.language
    
    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


# Init directory
dir = str(r'D:\Wilpo Millow\is_anyone_there')

language_sel = 'EN'

# Open window
window()


