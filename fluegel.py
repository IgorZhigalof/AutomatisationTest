from betterWindow import BetterWindow
from threading import Thread
import time

window = BetterWindow(0x0020A12)

def tpAction():
    window.sendChar("1")
    time.sleep(0.3)
    window.right_click_at(955, 538)
    time.sleep(0.5)
    window.sendChar("2")
    time.sleep(0.3)
    window.right_click_at(955, 538)
    time.sleep(0.3)

def script():
    count = 1
    window.sendChar("9")
    Thread(target=window.holdKey, args=("space", count * 2 + 1,)).start()
    Thread(target=window.holdKey, args=("shift", count * 2 + 1,)).start()
    for i in range(count):
        time.sleep(0.2)
        window.right_click_at(955, 538)
    time.sleep(0.1)
    tpAction()
    for j in range(5):
        time.sleep(0.7)
        window.sendChar(str(j + 3))
        time.sleep(0.2)
        window.left_click_at(955, 538)
    time.sleep(0.1)
    time.sleep(1)

def superScript():
    window.sendChar("8")
    time.sleep(1)
    window.right_click_at(955, 538)
    time.sleep(10)
    window.sendChar("2")
    time.sleep(0.3)
    window.right_click_at(955, 538)
    time.sleep(0.3)
    window.sendChar("7")
    time.sleep(0.3)
    window.left_click_at(955, 538)
    time.sleep(0.3)
    for i in range(4):
        time.sleep(1)
        for j in range(3):
            script()
            time.sleep(1)
    window.sendChar("9")
    time.sleep(0.3)
    window.left_click_at(955, 538)
    time.sleep(0.3)
    window.sendChar("q")
    time.sleep(0.3)
    window.sendChar("q")
    time.sleep(0.3)
    window.sendChar("q")

for i in range(100):
    superScript()
    time.sleep(5)


