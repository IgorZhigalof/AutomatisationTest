from Windows.betterWindowBuilder import BetterWindowBuilder
from threading import Thread
import time


windowBuilder = BetterWindowBuilder()
windowBuilder.setWindowTitle("Minecraft 1.7.10")
window = windowBuilder.build()

def hitAction(slot):
    print("hitAction")
    time.sleep(0.1)
    window.sendChar(str(slot))
    time.sleep(0.1)
    window.left_click_at(955, 538)
    time.sleep(0.1)

def script(count):
    print("script")
    hitAction(8)
    window.sendChar("9")
    Thread(target=window.holdKey, args=("shift", count * 2 + 1,)).start()
    for i in range(count):
        time.sleep(0.2)
        window.right_click_at(955, 538)
    time.sleep(1)
    tpAction()
    time.sleep(1)
    window.right_click_at(955, 538)
    for j in range(8):
        hitAction(j + 1)
    time.sleep(0.1)
    time.sleep(1)

def dropSoul():
    print("dropSoul")
    window.holdKey("9", 1)
    time.sleep(0.1)
    window.holdKey("q", 1)
    time.sleep(0.1)
    window.fastPressKey("9")
    time.sleep(0.1)
    window.fastPressKey("q")
    time.sleep(0.1)
    window.holdKey("9", 1)
    time.sleep(0.1)
    window.holdKey("q", 1)
    time.sleep(0.1)


def tpAction():
    window.fastPressKey("T")
    time.sleep(0.1)
    window.writeText("/home", 0.1)
    time.sleep(0.1)
    window.fastPressKey("enter")
    time.sleep(0.1)
    window.writeText("/tps", 0.1)
    window.fastPressKey("enter")


def superScript():
    print("superScript")
    count = 3
    time.sleep(0.2)
    tpAction()
    time.sleep(1)
    window.right_click_at(955, 538)
    time.sleep(1)
    for i in range(int(12/count)):
        script(count)
        color = window.get_pixel_color_from_window(770, 550)
        if color == (198, 198, 198):
            window.holdKey("esc", 1)
            break
        time.sleep(5)
        hitAction(8)
    tpAction()
    time.sleep(0.5)
    window.holdKey("a", 4)
    window.right_click_at(955, 538)
    dropSoul()
    time.sleep(2)
    time.sleep(2)


for i in range(100):
    superScript()


