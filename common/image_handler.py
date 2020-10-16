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

def into_direction():
    # into direction 指示界面
    pyautogui.press(']')
    # 弹出npc对话
    time.sleep(2)
    pyautogui.press(']')
    time.sleep(0.6)
    # select '结束'
    for i in range(5):
        time.sleep(0.3)
        # 将光标指向 结束
        pyautogui.press('l')
    time.sleep(0.8)
    # 点击结束ll
    pyautogui.press(']')
    time.sleep(0.8)
    # 左移光标至 重新委托
    pyautogui.press('k')
    time.sleep(0.5)
    # 点击 重新委托
    pyautogui.press(']')
    time.sleep(0.5)
    # 左移光标至 委托
    pyautogui.press('k')
    time.sleep(0.5)
    # 点击 委托
    pyautogui.press(']')
    time.sleep(0.8)
    # npc对话
    pyautogui.press(']')
    time.sleep(2)
    # 弹出界面，直接返回
    pyautogui.press('[')
    time.sleep(0.8)
    # npc对话返回
    pyautogui.press(']')
    # 等待主菜单
    time.sleep(2)
    return

def restart_work():
    # 点击结束
    pass

def back_exit():
    pyautogui.press('[')

def call_employee():
    for i in range(2):
        time.sleep(0.2)
        pyautogui.press(']')

if __name__ == '__main__':
    while True:
        time.sleep(2)
        call_employee()

        workdone_region = (665, 683, 669, 705)
        workdone_image = 'workdone.png'
        is_work_done(workdone_region, workdone_image)
        flag = True
        count = 0
        while flag:
            time.sleep(0.5)
            # 判断是否结束任务
            if is_work_done(workdone_region, workdone_image):
                # 则进入下一层
                into_direction()
                count = 0
            else:
                pyautogui.press('l')
                count += 1
            if count > 11:
                flag = False
                count = 0
                print("当前雇员全部正忙。。。")
                back_exit()
        # 等待5分钟后继续执行
        time.sleep(300)
