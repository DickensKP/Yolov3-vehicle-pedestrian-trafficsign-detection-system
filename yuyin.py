#语音模块
import pyttsx3
engine = pyttsx3.init()
def denglu():
    engine.say('系统登录成功')
    engine.runAndWait()
def cheliang():
    engine.say('正在载入车辆检测模块')
    engine.runAndWait()
def xingren():
    engine.say('正在载入行人检测模块')
    engine.runAndWait()
def biaozhi():
    engine.say('正在载入交通标志检测模块')
    engine.runAndWait()

def shishi():
    engine.say('开启实时检测')
    engine.runAndWait()
