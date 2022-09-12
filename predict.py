#对图片进行预测
from PIL import Image
from yolo import YOLO

if __name__ == "__main__":
    yolo = YOLO()
    mode = "predict"
    crop            = False#是否在单张图片预测后对目标进行截取
    count           = False#是否进行目标的计数
    while True:
        img = input('Input image filename:')
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image, crop=crop, count=count)
            r_image.show()


