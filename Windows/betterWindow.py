from Windows.window import Window
import time

class BetterWindow(Window):

    def __init__(self, hwnd):
        super().__init__(hwnd)

    def holdKey(self, key, tme):
        """The time parameter represents 100 milliseconds per unit."""
        for i in range(tme):
            self.key_down(key)
            time.sleep(0.1)
        self.key_up(key)

    def holdLeftClick(self, tme, x, y):
        for i in range(tme):
            self.left_click_at(x, y)
            time.sleep(0.1)
    def writeText(self, text:str):
        for chr in text:
            self.sendChar(chr)
            time.sleep(0.2)

    def fastPressKey(self, char: str):
        l_param = (self._scancodes[char.upper()] << 16) | 1
        self._user32.SendMessageA(self._hwnd,
                                  self._WM_KEYDOWN,
                                  self._scancodes[char.upper()],
                                  l_param
                                  )


