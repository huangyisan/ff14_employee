import pyautogui
import time

def judege_image(region, image):
    res = pyautogui.locateOnScreen(image=image, region=region, confidence=0.9)
    print(res)
    return res

def is_work_done(region, image):
    if judege_image(region, image):
        return True
    return False

def double_click_start():
    for i in range(2):
        time.sleep(0.2)
        pyautogui.press(']')

def click_v():
    time.sleep(1)
    pyautogui.press('v')


if __name__ == '__main__':
    work_region = (667, 678, 669, 694)
    work_image = 'startwork.png'
    time.sleep(2)
    while True:
        if judege_image(work_region,work_image):
            time.sleep(0.5)
            double_click_start()
            click_v()
        time.sleep(2)


