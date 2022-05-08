import pyautogui
import time


def autoplay(distance):
    if distance >= 240:
        pyautogui.mouseDown (400, 800)
        time.sleep (distance / 345)
        pyautogui.mouseUp (400, 800)

    elif distance >= 150:
        pyautogui.mouseDown (400, 800)
        time.sleep (distance / 355)
        pyautogui.mouseUp (400, 800)

    elif distance >= 100:
        pyautogui.mouseDown (400, 800)
        time.sleep (distance / 375)
        pyautogui.mouseUp (400, 800)

    elif 0 < distance < 100:
        pyautogui.mouseDown (400, 800)
        time.sleep (distance / 410)
        pyautogui.mouseUp (400, 800)

    elif distance == 0:
        # 遇到一些没有见过的方块导致无法识别，这个时候就无法判断了，需要人工处理
        pass


# 人工处理
def manualplay(x, y):
    # 需要先用print(pyautogui.position())获得两点坐标
    distance = ((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2) ** 0.5

    if distance >= 240:
        time.sleep (2)
        pyautogui.mouseDown (400, 800)
        time.sleep (distance / 345)
        pyautogui.mouseUp (400, 800)

    elif distance >= 150:
        time.sleep (2)
        pyautogui.mouseDown (400, 800)
        time.sleep (distance / 355)
        pyautogui.mouseUp (400, 800)

    elif distance >= 100:
        time.sleep (2)
        pyautogui.mouseDown (400, 800)
        time.sleep (distance / 375)
        pyautogui.mouseUp (400, 800)

    elif 0 < distance < 100:
        time.sleep (2)
        pyautogui.mouseDown (400, 800)
        time.sleep (distance / 410)
        pyautogui.mouseUp (400, 800)


# manualplay((184, 427), (277, 470))

# time.sleep(2)
# print(pyautogui.position())


