import time
import os
import sys

import cv2
import numpy as np
from PIL import Image

import pyautogui

# 以下2步可以把当前工作环境从Jump_Game文件夹中切换到主文件夹yolov5中
sys.path.append('F:/1/yolov5_jumpgame')  # 添加主路径到path路径中
os.chdir('F:/1/yolov5_jumpgame')  # 更改工作路径

from yolo import YOLO
from control import autoplay

if __name__ == "__main__":
    yolo = YOLO()

    # 使用屏幕内画面检测
    fps = 0.0
    while True:
        t1 = time.time()

        # 采取电脑屏幕，region参数为left, top, width, height
        img = pyautogui.screenshot(region=(0, 0, 447, 842))

        # 进行检测，获得图像和两个中心间的距离
        img, distance = yolo.detect_image (img)
        img = np.array (img)

        # RGBtoBGR满足opencv显示格式
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        # 自动玩跳一跳
        autoplay(distance)

        cv2.imshow('img', img)
        cv2.waitKey(1)

        time.sleep(1.5)
