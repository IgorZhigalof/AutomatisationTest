from window import Window
import time

class BetterWindow(Window):

    def __init__(self, window_id):
        super().__init__(window_id)

    def holdKey(self, key, tme):
        """The time parameter represents 100 milliseconds per unit."""
        for i in range(tme):
            self.key_down(key)
            time.sleep(0.1)
        self.key_up(key)

    def writeText(self, text:str):
        for chr in text:
            self.sendChar(chr)
            time.sleep(0.2)

    def fastPressKey(self, char: str):
        l_param = (self._scancodes[char.upper()] << 16) | 1
        self._user32.SendMessageA(self._window_id,
                                  self._WM_KEYDOWN,
                                  self._scancodes[char.upper()],
                                  l_param
                                  )
