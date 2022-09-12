#对视频进行预测
import time
import cv2
import numpy as np
from PIL import Image

from yolo import YOLO

yolo = YOLO()
mode = "video"
video_path      = '信号灯.mp4'
video_save_path = "predict信号灯.mp4"
video_fps       = 25.0

capture = cv2.VideoCapture(video_path)

fourcc  = cv2.VideoWriter_fourcc(*'XVID')
size    = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out     = cv2.VideoWriter(video_save_path, fourcc, video_fps, size)

ref, frame = capture.read()
if not ref:
    raise ValueError("未能正确读取视频，请注意是否正确填写视频路径。")

fps = 0.0
while(True):
    t1 = time.time()
    ref, frame = capture.read()
    if not ref:
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = Image.fromarray(np.uint8(frame))
    frame = np.array(yolo.detect_image(frame))
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    fps  = ( fps + (1./(time.time()-t1)) ) / 2
    print("fps= %.2f"%(fps))
    frame = cv2.putText(frame, "fps= %.2f"%(fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("video",frame)
    c= cv2.waitKey(1) & 0xff

    out.write(frame)

    if c==27:
        capture.release()#按Esc退出
        break

capture.release()

print("Save processed video to the path :" + video_save_path)
out.release()

cv2.destroyAllWindows()


