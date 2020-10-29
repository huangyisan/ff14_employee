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
    for i in range(1):
        time.sleep(0.2)
        pyautogui.press(']')

def click_v():
    time.sleep(1)
    pyautogui.press('v')


if __name__ == '__main__':
    # work_region = (667, 678, 669, 694)
    work_region = (1767, 632, 1903, 661)
    work_image = 'startwork.png'
    time.sleep(2)
    press_v = ''
    while True:
        if judege_image(work_region,work_image):
            double_click_start()
            press_v = False
        else:
            if not press_v:
                time.sleep(0.5)
                click_v()
                press_v = True
        time.sleep(0.5)


