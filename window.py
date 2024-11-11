import ctypes


class Window:
    _user32 = ctypes.WinDLL('user32.dll')
    _scancodes = dict()
    _window_id = ""
    _WM_KEYDOWN = 0x0100
    _WM_KEYUP = 0x0101
    _WM_CHAR = 0x0102
    _WM_LBUTTONDOWN = 0x0201
    _WM_LBUTTONUP = 0x0202
    _WM_MOUSEMOVE = 0x0200
    _WM_RBUTTONDOWN = 0x0204
    _WM_RBUTTONUP = 0x0205

    def __init__(self, window_id):
        self._window_id = window_id
        scancodes_file = open("scancodes.txt", "r")
        content = scancodes_file.readlines()

        for line in content:
            line = line.replace("\n", "")
            split = line.split("\t")
            self._scancodes[split[0]] = int(split[1], 16)
        print(self._scancodes)

    def key_down(self, char:str):
        l_param = (self._scancodes[char.upper()] << 16) | 1
        self._user32.SendMessageA(self._window_id,
                                   self._WM_KEYDOWN,
                                   self._scancodes[char.upper()],
                                   l_param
                                   )
        try:
            symbol = ord(char)
            self._user32.SendMessageA(self._window_id, self._WM_CHAR, symbol, l_param)
        except TypeError:
            pass

    def key_up(self, char:str):
        l_param = (self._scancodes[char.upper()] << 16) | 1
        self._user32.SendMessageA(self._window_id,
                                   self._WM_KEYUP,
                                   self._scancodes[self._charFormatter(char)],
                                   l_param | (1 << 31)
                                   )

    def sendChar(self, char:str):
        l_param = (self._scancodes[self._charFormatter(char)] << 16) | 1
        self.key_down(char)
        self.key_up(char)

    def left_click_at(self, x, y):
        lParam = y * 65535 + x + y
        self._user32.SendMessageA(self._window_id, self._WM_MOUSEMOVE, 0, lParam)
        self._user32.SendMessageA(self._window_id, self._WM_LBUTTONDOWN, 0x0001, lParam)
        self._user32.SendMessageA(self._window_id, self._WM_LBUTTONUP, 0x0001, lParam)

    def right_click_at(self, x, y):
        lParam = y * 65535 + x + y
        self._user32.SendMessageA(self._window_id, self._WM_MOUSEMOVE, 0, lParam)
        self._user32.SendMessageA(self._window_id, self._WM_RBUTTONDOWN, 0x0001, lParam)
        self._user32.SendMessageA(self._window_id, self._WM_RBUTTONUP, 0x0001, lParam)

    def _charFormatter(self, char:str):
        if (char in "\\"):
            return char
        else:
            return char.upper()




