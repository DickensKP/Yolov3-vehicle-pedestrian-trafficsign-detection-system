from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel
from PyQt5.QtGui import QPixmap
import sys
import resource_rc
from de import Ui_Form
from de1 import  Ui_Form1
from de2 import  Ui_Form2
from de3 import  Ui_Form3
from de4 import  Ui_Form4

class myui(QMainWindow,Ui_Form):
    def __init__(self):
        super(myui,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('库里能力分析')

class myui1(QMainWindow,Ui_Form1):
    def __init__(self):
        super(myui1,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('库里场均得分')
        self.setGeometry(500,30,1000,1100)
        self.initUI()
    def initUI(self):
        lbl = QLabel('图片',self)
        lbl.setPixmap(QPixmap('./场均得分.png'))
        lbl.resize(1000,1000)
        lbl.setScaledContents(True)
    def open(self):
        self.show()

class myui2(QMainWindow,Ui_Form2):
    def __init__(self):
        super(myui2,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('库里命中率')
        self.setGeometry(500,30,1000,1100)
        self.initUI()
    def initUI(self):
        lbl = QLabel('图片',self)
        lbl.setPixmap(QPixmap('./命中率.png'))
        lbl.resize(1000,1000)
        lbl.setScaledContents(True)
    def open(self):
        self.show()

class myui3(QMainWindow,Ui_Form3):
    def __init__(self):
        super(myui3,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('库里原始数据')
        self.setGeometry(500,30,1000,1100)
        self.initUI()
    def initUI(self):
        lbl = QLabel('图片',self)
        lbl.setPixmap(QPixmap('./库里原始数据.png'))
        lbl.resize(1000,1000)
        lbl.setScaledContents(True)
    def open(self):
        self.show()

class myui4(QMainWindow,Ui_Form4):
    def __init__(self):
        super(myui4,self).__init__()
        self.setupUi(self)
        self.setGeometry(500,100,1000,800)
        self.initUI()
    def initUI(self):
        lbl = QLabel('图片',self)
        lbl.setPixmap(QPixmap('./库里p图.jpg'))
        lbl.resize(900,500)
        lbl.setScaledContents(True)
    def open(self):
        self.show()

class myui41(QMainWindow,Ui_Form3):
    def __init__(self):
        super(myui41,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('天旋地转')
        self.setGeometry(500,30,1000,1100)
        self.initUI()
    def initUI(self):
        lbl = QLabel('图片',self)
        lbl.setPixmap(QPixmap('./天旋地转.png'))
        lbl.resize(1000,1000)
        lbl.setScaledContents(True)
    def open(self):
        self.show()

class myui42(QMainWindow,Ui_Form3):
    def __init__(self):
        super(myui42,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('变色龙')
        self.setGeometry(500,30,1000,1100)
        self.initUI()
    def initUI(self):
        lbl = QLabel('图片',self)
        lbl.setPixmap(QPixmap('./变色龙.png'))
        lbl.resize(1000,1000)
        lbl.setScaledContents(True)
    def open(self):
        self.show()

class myui43(QMainWindow,Ui_Form3):
    def __init__(self):
        super(myui43,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('无头勇士')
        self.setGeometry(500,30,1000,1100)
        self.initUI()
    def initUI(self):
        lbl = QLabel('图片',self)
        lbl.setPixmap(QPixmap('./无头勇士.png'))
        lbl.resize(1000,1000)
        lbl.setScaledContents(True)
    def open(self):
        self.show()

class myui44(QMainWindow,Ui_Form3):
    def __init__(self):
        super(myui44,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('无名勇士')
        self.setGeometry(500,30,1000,1100)
        self.initUI()
    def initUI(self):
        lbl = QLabel('图片',self)
        lbl.setPixmap(QPixmap('./无名勇士.png'))
        lbl.resize(1000,1000)
        lbl.setScaledContents(True)
    def open(self):
        self.show()

class myui45(QMainWindow,Ui_Form3):
    def __init__(self):
        super(myui45,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('一键瘦身')
        self.setGeometry(800,30,500,1100)
        self.initUI()
    def initUI(self):
        lbl = QLabel('图片',self)
        lbl.setPixmap(QPixmap('./一键瘦身.png'))
        lbl.resize(500,1000)
        lbl.setScaledContents(True)
    def open(self):
        self.show()

class myui46(QMainWindow,Ui_Form3):
    def __init__(self):
        super(myui46,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('透明勇士')
        self.setGeometry(500,30,1000,1100)
        self.initUI()
    def initUI(self):
        lbl = QLabel('图片',self)
        lbl.setPixmap(QPixmap('./透明勇士.png'))
        lbl.resize(1000,1000)
        lbl.setScaledContents(True)
    def open(self):
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = myui()
    child1 = myui1()
    child2 = myui2()
    child3 = myui3()
    child4 = myui4()

    child41 = myui41()
    child42 = myui42()
    child43 = myui43()
    child44 = myui44()
    child45 = myui45()
    child46 = myui46()

    main.show()
    main.pushButton2.clicked.connect(child1.open)
    main.pushButton.clicked.connect(child2.open)
    main.pushButton3.clicked.connect(child3.open)
    main.pushButton4.clicked.connect(child4.open)

    child4.pushButton_1.clicked.connect(child41.open)
    child4.pushButton_2.clicked.connect(child42.open)
    child4.pushButton_3.clicked.connect(child43.open)
    child4.pushButton_4.clicked.connect(child44.open)
    child4.pushButton_5.clicked.connect(child45.open)
    child4.pushButton_6.clicked.connect(child46.open)
    sys.exit(app.exec_())
