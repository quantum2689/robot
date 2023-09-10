import serial
from frontend import  Ui_forward
import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut
serial_port = "COM3"


class main_window(qtw.QMainWindow, Ui_forward):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.forward_2.clicked.connect(self.Forward) 
        self.backward.clicked.connect(self.Backward)
        self.left.clicked.connect(self.Left)
        self.right.clicked.connect(self.Right)
        self.up.clicked.connect(self.hand_up)
        self.down.clicked.connect(self.hand_down)
        self.shortcut=QShortcut(QKeySequence("w"),self)
        self.shortcut.activated.connect(self.Forward)
        self.shortcut=QShortcut(QKeySequence("s"),self)
        self.shortcut.activated.connect(self.Backward)
        self.shortcut=QShortcut(QKeySequence("d"),self)
        self.shortcut.activated.connect(self.Right)
        self.shortcut=QShortcut(QKeySequence("a"),self)
        self.shortcut.activated.connect(self.Left)
        self.ser = serial.Serial(serial_port)  
        self.shortcut=QShortcut(QKeySequence("up"),self)
        self.shortcut.activated.connect(self.hand_up)
        self.shortcut=QShortcut(QKeySequence("down"),self)
        self.shortcut.activated.connect(self.hand_down)


    def Forward(self):
        print("moving forward")
        self.ser.write(b'w')     

    def Backward(self):
        print("moving backward")
        self.ser.write(b"S")
    def Left(self):
        print("moving left")
        self.ser.write(b'A')    
    def Right(self):
        print("moving right")
        self.ser.write(b'D')     
    def hand_up(self):
        print("hand up")
        self.ser.write(b'up')    
    def hand_down(self):
        print("hand down")
        self.ser.write(b'down')   
         
    def slider(self):
        pass
    

if __name__ == "__main__":
    app = qtw.QApplication([])
    ui = main_window()
    ui.show()
    app.exec()