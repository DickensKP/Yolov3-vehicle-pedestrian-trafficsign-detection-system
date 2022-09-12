from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import  QtGui, QtWidgets
import sys,cv2,time
from PIL import Image
import numpy as np
import resource_rc

from 登录 import denglu
from 关于 import guanyu
from 主页面 import  zhuyemian
from 副标志 import  fubiaozhi
from 副车辆 import fucheliang
from 副行人 import fuxingren
from mAP指标 import mAP

import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from yolo import YOLO
import autofile
import yuyin

yolo = YOLO()
class denglujiemian(QMainWindow,denglu):
    def __init__(self):
        super(denglujiemian,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('登录')
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton2.clicked.connect(self.ok)
    def ok(self):
        text1 = self.lineEdit.text()
        text2 = self.lineEdit_2.text()
        if text1 == 'admin' and text2 == 'admin':
            child2.open()
            main.close()
            yuyin.denglu()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

class guanyujiemian(QMainWindow,guanyu):
    def __init__(self):
        super(guanyujiemian,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('关于')
    def open(self):
        self.show()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

class zhujiemian(QMainWindow,zhuyemian):
    def __init__(self):
        super(zhujiemian,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('主界面')
    def open(self):
        self.show()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
##############################################################################################################################
class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5):
        fig = Figure(figsize=(width, height),dpi=73)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.ax = fig.add_subplot(111)
class Figure_Canvas1(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5):
        fig = Figure(figsize=(width, height),dpi=73)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.ax1 = fig.add_subplot(111)
class biaozhijiemian(QMainWindow,fubiaozhi):
    def __init__(self):
        super(biaozhijiemian,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('交通标志识别')

        self.capture = cv2.VideoCapture(0)
        self.cap = cv2.VideoCapture(0)
        self.timer_camera = QTimer()

        self.pushButton2_7.clicked.connect(self.slotStart)
        self.pushButton2_7.clicked.connect(yuyin.shishi)
        self.pushButton2_11.clicked.connect(self.slotStop)

        self.pushButton2_5.clicked.connect(self.openimg)
        self.pushButton2_12.clicked.connect(self.dealwithimg)

        self.pushButton2_6.clicked.connect(self.openvideo)
        self.pushButton2_4.clicked.connect(self.dealwithvideo)

        self.pushButton2_8.clicked.connect(self.report)
        self.pushButton2_8.clicked.connect(self.reportreport)

    def report(self):
        Warming = QMessageBox.warning(self, "恭喜", "交通标志识别报告已导出",
                                      QMessageBox.Yes)
    def reportreport(self):
        self.reporttext = self.openfile_name[0].replace('jpg','txt').replace('img','map_out')
        self.imgname = self.openfile_name[0].replace('jpg','png').replace('img','img_out')
        autofile.pdf(self.imgname,self.reporttext)
    def openimg(self):
        self.openfile_name = QFileDialog.getOpenFileName(self,'选择图片','./img', "All Files(*)")
        self.lineEdit_2.setText(self.openfile_name[0])
        self.label_2.setPixmap(QPixmap(self.openfile_name[0]))
        self.label_2.setScaledContents(True)
    def dealwithimg(self):
        self.dealwithimgname = self.openfile_name[0].replace('jpg','png').replace('img','img_out')
        self.lineEdit_2.setText(self.dealwithimgname)
        self.label_2.setPixmap(QPixmap(self.dealwithimgname))
        self.label_2.setScaledContents(True)
    def openvideo(self):
        self.videoName, imgType = QFileDialog.getOpenFileName(self, "选择视频", "./img", "*.mp4;;All Files(*)")
        self.lineEdit_2.setText(self.videoName)
        self.cap = cv2.VideoCapture(self.videoName)
        self.timer_camera.start(100)
        self.timer_camera.timeout.connect(self.openFrame)
    def dealwithvideo(self):
        self.videoName = self.videoName.replace('信号灯','predict信号灯')
        self.lineEdit_2.setText(self.videoName)
        self.cap = cv2.VideoCapture(self.videoName)
        self.timer_camera.start(100)
        self.timer_camera.timeout.connect(self.openFrame)
    def openFrame(self):
        if (self.cap.isOpened()):
            ret, self.frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                height, width, bytesPerComponent = frame.shape
                bytesPerLine = bytesPerComponent * width
                q_image = QImage(frame.data, width, height, bytesPerLine,
                                 QImage.Format_RGB888).scaled(self.label.width(), self.label.height())
                self.label_2.setPixmap(QPixmap.fromImage(q_image))
                self.label_2.setScaledContents(True)
            else:
                self.cap.release()
                self.timer_camera.stop()
    def slotStop(self):
        if self.cap != []:
            self.capture.release()
            self.timer_camera.stop()
            self.label_2.setText("本地摄像头被关闭")
            self.label_2.setStyleSheet("QLabel{background:white;}"
                                       "QLabel{color:rgb(100,100,100);font-size:100px;font-weight:bold;font-family:宋体;}"
                                       )
        else:
            Warming = QMessageBox.warning(self, "警告", "请先打开摄像头",
                                          QMessageBox.Yes)
    def slotStart(self):
        fps = 0.0
        t1 = time.time()
        while True:
            ret, im = self.capture.read()
            if im is None:
                break
            frame = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(np.uint8(frame))
            frame = np.array(yolo.detect_image(frame))
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            pic = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0],
                               QtGui.QImage.Format_BGR888)
            with open('all.txt','r',encoding='utf-8') as fo:
                all = fo.read()
            fps = (fps + (1. / (time.time() - t1))) / 2
            frame = cv2.putText(frame, f'Total_box={all}', (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            self.label_2.setPixmap(QtGui.QPixmap.fromImage(pic))
            self.label_2.setScaledContents(True)
            cv2.waitKey(1)

            self.dr = Figure_Canvas()
            graphicscene = QtWidgets.QGraphicsScene()
            graphicscene.addWidget(self.dr)
            self.dr.ax.set_xlim(1)
            self.dr.ax.set_ylim(0, 0.5)
            self.bar = self.dr.ax.bar(np.array(1), np.array(fps), width=0.4)
            self.dr.ax.set_title('FPS')
            self.patches = self.bar.patches
            self.graphicsView_2.setScene(graphicscene)
            self.graphicsView_2.show()

            self.dr1 = Figure_Canvas1()
            graphicscene1 = QtWidgets.QGraphicsScene()
            graphicscene1.addWidget(self.dr1)
            self.dr1.ax1.set_ylim(0, 4)
            with open('num.txt', 'r', encoding='utf-8') as fo:
                num = fo.read()
            a = num.replace('[', '').replace(']', '').replace('.', '').split()
            num = list(map(int, a))
            labels = ['speedlimit', 'crosswalk', 'trafficlight', 'stop']
            self.bar = self.dr1.ax1.bar(labels, np.array(num), width=0.5)
            self.dr1.ax1.set_title('classes_num')
            self.patches = self.bar.patches
            self.graphicsView.setScene(graphicscene1)
            self.graphicsView.show()
        self.capture.release()
        cv2.destroyAllWindows()
    def open(self):
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

class mAPjiemian(QMainWindow,mAP):
    def __init__(self):
        super(mAPjiemian,self).__init__()
        self.setupUi(self)
        self.setWindowTitle('交通标志识别')
        self.pushButton2_6.clicked.connect(self.openimg1)
        self.pushButton2_8.clicked.connect(self.openimg2)
        self.pushButton2_7.clicked.connect(self.openimg3)
        self.pushButton2_9.clicked.connect(self.openimg4)
        self.pushButton2_10.clicked.connect(self.openimg5)

    def openimg1(self):
        self.label_2.setPixmap(QPixmap('speedlimit.png'))
        self.label_2.setScaledContents(True)
    def openimg2(self):
        self.label_2.setPixmap(QPixmap('crosswalk.png'))
        self.label_2.setScaledContents(True)
    def openimg3(self):
        self.label_2.setPixmap(QPixmap('mAP.png'))
        self.label_2.setScaledContents(True)
    def openimg4(self):
        self.label_2.setPixmap(QPixmap('trafficlight.png'))
        self.label_2.setScaledContents(True)
    def openimg5(self):
        self.label_2.setPixmap(QPixmap('stop.png'))
        self.label_2.setScaledContents(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
    def open(self):
        self.show()

class cheliangjiemian(QMainWindow, fucheliang):
    def __init__(self):
        super(cheliangjiemian, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('车辆识别')

        self.cap = []
        self.timer_camera = QTimer()

        self.pushButton2_5.clicked.connect(self.openimg)
        self.pushButton2_12.clicked.connect(self.dealwithimg)

        self.pushButton2_6.clicked.connect(self.openvideo)
        self.pushButton2_4.clicked.connect(self.dealwithvideo)
        self.pushButton2_9.clicked.connect(self.slotStop)
    def openimg(self):
        self.openfile_name = QFileDialog.getOpenFileName(self, '选择图片', './img', "All Files(*)")
        self.lineEdit_2.setText(self.openfile_name[0])
        self.label_2.setPixmap(QPixmap(self.openfile_name[0]))
        self.label_2.setScaledContents(True)
    def dealwithimg(self):
        self.dealwithimgname = self.openfile_name[0].replace('img', 'img_out')
        self.lineEdit_2.setText(self.dealwithimgname)
        self.label_2.setPixmap(QPixmap(self.dealwithimgname))
        self.label_2.setScaledContents(True)
    def openvideo(self):
        self.videoName, imgType = QFileDialog.getOpenFileName(self, "选择视频", "./img", "*.mp4;;All Files(*)")
        self.lineEdit_2.setText(self.videoName)
        self.cap = cv2.VideoCapture(self.videoName)
        self.timer_camera.start(100)
        self.timer_camera.timeout.connect(self.openFrame)
    def dealwithvideo(self):
        self.videoName = self.videoName.replace('车辆', 'predict车辆')
        self.lineEdit_2.setText(self.videoName)
        self.cap = cv2.VideoCapture(self.videoName)
        self.timer_camera.start(100)
        self.timer_camera.timeout.connect(self.openFrame)
    def openFrame(self):  ##打开视频
        if (self.cap.isOpened()):
            ret, self.frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                height, width, bytesPerComponent = frame.shape
                bytesPerLine = bytesPerComponent * width
                q_image = QImage(frame.data, width, height, bytesPerLine,
                                 QImage.Format_RGB888).scaled(self.label.width(), self.label.height())
                self.label_2.setPixmap(QPixmap.fromImage(q_image))
                self.label_2.setScaledContents(True)
            else:
                self.cap.release()
                self.timer_camera.stop()
    def slotStop(self):
        if self.cap != []:
            self.cap.release()
            self.timer_camera.stop()
            self.label_2.setText("视频被关闭")
            self.label_2.setStyleSheet("QLabel{background:white;}"
                                       "QLabel{color:rgb(100,100,100);font-size:180px;font-weight:bold;font-family:宋体;}"
                                       )
        else:
            Warming = QMessageBox.warning(self, "警告", "请先打开视频",
                                          QMessageBox.Yes)
    def open(self):
        self.show()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

class xingrenjiemian(QMainWindow, fuxingren):
    def __init__(self):
        super(xingrenjiemian, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('行人识别')

        self.cap = []
        self.timer_camera = QTimer()

        self.pushButton2_5.clicked.connect(self.openimg)
        self.pushButton2_12.clicked.connect(self.dealwithimg)

        self.pushButton2_6.clicked.connect(self.openvideo)
        self.pushButton2_4.clicked.connect(self.dealwithvideo)
        self.pushButton2_9.clicked.connect(self.slotStop)
    def openimg(self):
        self.openfile_name = QFileDialog.getOpenFileName(self, '选择图片', './img', "All Files(*)")
        self.lineEdit_2.setText(self.openfile_name[0])
        self.label_2.setPixmap(QPixmap(self.openfile_name[0]))
        self.label_2.setScaledContents(True)
    def dealwithimg(self):
        self.dealwithimgname = self.openfile_name[0].replace('img', 'img_out')
        self.lineEdit_2.setText(self.dealwithimgname)
        self.label_2.setPixmap(QPixmap(self.dealwithimgname))
        self.label_2.setScaledContents(True)
    def openvideo(self):
        self.videoName, imgType = QFileDialog.getOpenFileName(self, "选择视频", "./img", "*.mp4;;All Files(*)")
        self.lineEdit_2.setText(self.videoName)
        self.cap = cv2.VideoCapture(self.videoName)
        self.timer_camera.start(100)
        self.timer_camera.timeout.connect(self.openFrame)
    def dealwithvideo(self):
        self.videoName = self.videoName.replace('行人','predict行人')
        self.lineEdit_2.setText(self.videoName)
        self.cap = cv2.VideoCapture(self.videoName)
        self.timer_camera.start(100)
        self.timer_camera.timeout.connect(self.openFrame)
    def openFrame(self):  ##打开视频
        if (self.cap.isOpened()):
            ret, self.frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                height, width, bytesPerComponent = frame.shape
                bytesPerLine = bytesPerComponent * width
                q_image = QImage(frame.data, width, height, bytesPerLine,
                                 QImage.Format_RGB888).scaled(self.label.width(), self.label.height())
                self.label_2.setPixmap(QPixmap.fromImage(q_image))
                self.label_2.setScaledContents(True)
            else:
                self.cap.release()
                self.timer_camera.stop()
    def slotStop(self):
        if self.cap != []:
            self.cap.release()
            self.timer_camera.stop()
            self.label_2.setText("视频被关闭")
            self.label_2.setStyleSheet("QLabel{background:white;}"
                                       "QLabel{color:rgb(100,100,100);font-size:180px;font-weight:bold;font-family:宋体;}"
                                       )
        else:
            Warming = QMessageBox.warning(self, "警告", "请先打开视频",
                                          QMessageBox.Yes)
    def open(self):
        self.show()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main =  denglujiemian()
    child1 = guanyujiemian()
    child2 = zhujiemian()
    child21 = biaozhijiemian()
    child22 = cheliangjiemian()
    child23 = xingrenjiemian()

    child211 = mAPjiemian()

    main.show()

    main.pushButton2_4.clicked.connect(child1.open)

    child2.pushButton2_7.clicked.connect(child21.open)
    child2.pushButton2_5.clicked.connect(child22.open)
    child2.pushButton2_6.clicked.connect(child23.open)

    child2.pushButton2_7.clicked.connect(yuyin.biaozhi)
    child2.pushButton2_5.clicked.connect(yuyin.cheliang)
    child2.pushButton2_6.clicked.connect(yuyin.xingren)

    child21.pushButton2_10.clicked.connect(child211.open)

    sys.exit(app.exec_())