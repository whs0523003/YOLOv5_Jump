import os
import sys

import numpy as np
import cv2
import pyautogui

# 以下2步可以把当前工作环境从Jump_Game文件夹中切换到主文件夹yolov5中
sys.path.append('F:/1/yolov5')  # 添加主路径到path路径中
os.chdir('F:/1/yolov5')  # 更改工作路径

# 每隔几秒保存一下屏幕的画面，名字为img1，img2，img3...，用于制作数据集
i = 1
while True:
    img = pyautogui.screenshot(region=(0, 0, 447, 842))
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    cv2.imshow('s', frame)

    cv2.imwrite('Game_Jump/dataset/'+str(i)+'.jpg', frame)

    cv2.waitKey(4000)
    i += 1

    cv2.destroyAllWindows()