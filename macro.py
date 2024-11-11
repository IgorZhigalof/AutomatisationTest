from betterWindow import BetterWindow
from threading import Thread
import time

window = BetterWindow(0x0D011E2)

window.fastPressKey("t")
time.sleep(1)
window.writeText("/рщьу")
time.sleep(1)
window.fastPressKey("enter")
time.sleep(1)
window.sendChar("1")
time.sleep(1)
window.right_click_at(955, 538)
time.sleep(1)
window.fastPressKey("esc")
