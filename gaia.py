import threading

from window import Window
from threading import Thread
import time


window = Window(0x0C81260)

def holdShift(shift_cd):
    for i in range(shift_cd * 10 + 5):
        window.key_down("shift")
        time.sleep(0.1)
    window.key_up("shift")

def script():
    shift_cd = 4
    window.sendChar("1")
    Thread(target=holdShift, args=(shift_cd,)).start()
    time.sleep(0.1)
    for i in range(8):
        window.right_click_at(955, 538)
        time.sleep(shift_cd/8)
    time.sleep(20)
    for i in range(8):
        time.sleep(0.1)
        window.sendChar(str(i + 2))
        time.sleep(shift_cd/8)
        window.left_click_at(955, 538)


for i in range(300):
    script()
    time.sleep(20)
