#车辆识别图片
import paddlehub as hub
import cv2

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import os

vehicles_detector = hub.Module(name="yolov3_darknet53_vehicles")

test_img_path = "car.jpg"

img1 = mpimg.imread(test_img_path)
plt.figure(figsize=(10,10))

result =  vehicles_detector.object_detection(images=[cv2.imread(test_img_path)],output_dir = 'output')

res = os.listdir('output')
img1 = mpimg.imread('output/' + res[len(res)-1])

plt.figure(figsize=(10,10))
plt.imshow(img1)

