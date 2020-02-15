import pyautogui

# 1、屏幕随机移动
# import random

# print(pyautogui.size())
# print(pyautogui.position())

# i = 0
# while i < 10:
#     x = random.randint(0, pyautogui.size().width)
#     y = random.randint(0, pyautogui.size().height)
#     pyautogui.moveTo(x, y, duration=1)
#     print("x = %d , y = %d" % (x, y))
#     i += 1


# ===============================================
# //2、自定义鼠标反复移动
error = True
while error:
    try:
        time = int(input("请输入鼠标操作总时间（单位：秒）\n"))
        interval = float(input("请输入鼠标操作间隔时间，可以是小数（单位：秒）\n"))
        length = int(input("请输入鼠标移动距离（单位：像素）\n"))
        error = False

        print("正在自动移动鼠标，如果想要取消移动，可以手动移动鼠标超过屏幕范围的1/4即可。")

        currentX = pyautogui.position().x
        currentY = pyautogui.position().y

        i = 0
        times = 1
        while times <= time / interval:
            if pyautogui.position().x - currentX >= int(
                    pyautogui.size().width / 4) | pyautogui.position().y - currentY >= int(pyautogui.size().height / 4):
                print("检测到鼠标移动范围超过屏幕范围的1/4，自动停止程序，已为您自动摸鱼 %f 秒" % (times * interval))
                break

            if i == 0:
                currentX += length
                currentY += length
                print("x = %d , y = %d" % (currentX, currentY))
                i = 1
            else:
                currentX -= length
                currentY -= length
                print("x = %d , y = %d" % (currentX, currentY))
                i = 0
            times += 1
            pyautogui.moveTo(currentX, currentY, 0.5)
            pyautogui.sleep(interval)
        else:
            print("已为您自动摸鱼 %d 秒!" % time)
    except ValueError:
        error = True
        print("请仔细校验输入参数是否合法！！！")
