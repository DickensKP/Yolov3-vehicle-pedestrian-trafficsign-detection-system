#车辆识别视频
import cv2
import os
import paddlehub as hub

vehicles_detector = hub.Module(name="yolov3_darknet53_vehicles")

def get_combine_img(img_path,vehicles_detector=vehicles_detector):
    result = vehicles_detector.object_detection(paths=[img_path])
    image=cv2.imread(img_path)
    return image
input_video = 'video.mp4'

def transform_video_to_image(video_file_path, img_path):
    video_capture = cv2.VideoCapture(video_file_path)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    count = 0
    while(True):
        ret, frame = video_capture.read()
        if ret:
            cv2.imwrite(img_path + '%d.jpg' % count, frame)
            count += 1
        else:
            break
    video_capture.release()
    print('视频图片保存成功, 共有 %d 张' % count)
    return fps

fps = transform_video_to_image(input_video, 'frame/')

def analysis_pose(input_frame_path, output_frame_path, is_print=True):
    file_items = os.listdir(input_frame_path)
    file_len = len(file_items)

    for i, file_item in enumerate(file_items):
        if is_print:
            print(i+1,'/', file_len, ' ', os.path.join(output_frame_path, file_item))
        combine_img = get_combine_img(os.path.join(input_frame_path, file_item))
        cv2.imwrite(os.path.join(output_frame_path, file_item), combine_img)
analysis_pose('frame/', 'output/', is_print=True)

def combine_image_to_video(comb_path, output_file_path, fps=30, is_print=False):
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    file_items = os.listdir(comb_path)
    file_len = len(file_items)
    if file_len > 0 :
        temp_img = cv2.imread(os.path.join(comb_path, file_items[0]))
        img_height, img_width = temp_img.shape[0], temp_img.shape[1]
        out = cv2.VideoWriter(output_file_path, fourcc, fps, (img_width, img_height))

        for i in range(file_len):
            pic_name = os.path.join(comb_path, str(i)+".jpg")
            if is_print:
                print(i+1,'/', file_len, ' ', pic_name)
            img = cv2.imread(pic_name)
            out.write(img)
        out.release()
combine_image_to_video('yolov3_vehicles_detect_output/', 'analysis.mp4', fps)


