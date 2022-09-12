#打开摄像头
import time
import cv2
import numpy as np
from PIL import Image

from yolo import YOLO

yolo = YOLO()
cap = cv2.VideoCapture(0)

while (True):
    ref, frame = cap.read()
    t1 = time.time()  # 读取某一帧
    if not ref:
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = Image.fromarray(np.uint8(frame))
    frame = np.array(yolo.detect_image(frame))
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)


    cv2.imshow("video",frame)
    c= cv2.waitKey(1) & 0xff

    if c==27:
        cap.release()#按Esc退出
        break

cap.release()

cv2.destroyAllWindows()

