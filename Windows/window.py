import ctypes
import time
from ctypes import wintypes

class RECT(ctypes.Structure):
    _fields_ = [
        ("left", wintypes.LONG),
        ("top", wintypes.LONG),
        ("right", wintypes.LONG),
        ("bottom", wintypes.LONG)
    ]

WM_ACTIVATE = 0x0006
WA_ACTIVE = 1

class Window:
    _user32 = ctypes.WinDLL('user32.dll')
    _gdi32 = ctypes.windll.gdi32
    _hdc = ""
    _scancodes = dict()
    _hwnd = ""
    _WM_KEYDOWN = 0x0100
    _WM_KEYUP = 0x0101
    _WM_CHAR = 0x0102
    _WM_LBUTTONDOWN = 0x0201
    _WM_LBUTTONUP = 0x0202
    _WM_MOUSEMOVE = 0x0200
    _WM_RBUTTONDOWN = 0x0204
    _WM_RBUTTONUP = 0x0205

    def __init__(self, hwnd):
        self._hwnd = hwnd
        scancodes_file = open("Windows/scancodes.txt", "r")
        content = scancodes_file.readlines()

        for line in content:
            line = line.replace("\n", "")
            split = line.split("\t")
            self._scancodes[split[0]] = int(split[1], 16)
        print(self._scancodes)

    def key_down(self, char:str):
        l_param = (self._scancodes[char.upper()] << 16) | 1
        self._user32.SendMessageA(self._hwnd,
                                  self._WM_KEYDOWN,
                                  self._scancodes[char.upper()],
                                  l_param
                                  )
        try:
            symbol = ord(char)
            self._user32.SendMessageA(self._hwnd, self._WM_CHAR, symbol, l_param)
        except TypeError:
            pass

    def key_up(self, char:str):
        l_param = (self._scancodes[char.upper()] << 16) | 1
        self._user32.SendMessageA(self._hwnd,
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
        self._user32.SendMessageA(self._hwnd, self._WM_MOUSEMOVE, 0, lParam)
        time.sleep(0.1)
        self._user32.SendMessageA(self._hwnd, self._WM_LBUTTONDOWN, 0x0001, lParam)
        time.sleep(0.1)
        self._user32.SendMessageA(self._hwnd, self._WM_LBUTTONUP, 0x0001, lParam)

    def right_click_at(self, x, y):
        lParam = y * 65535 + x + y
        self._user32.SendMessageA(self._hwnd, self._WM_MOUSEMOVE, 0, lParam)
        self._user32.SendMessageA(self._hwnd, self._WM_RBUTTONDOWN, 0x0001, lParam)
        self._user32.SendMessageA(self._hwnd, self._WM_RBUTTONUP, 0x0001, lParam)

    def _charFormatter(self, char:str):
        if (char in "\\"):
            return char
        else:
            return char.upper()

    # Структура для хранения прямоугольника (границ окна)
    def get_pixel_color_from_window(self, x, y):
        """
        Получает цвет пикселя в координатах (x, y) относительно окна с дескриптором hwnd.

        :param hwnd: HWND (дескриптор окна)
        :param x: Координата X относительно окна
        :param y: Координата Y относительно окна
        :return: Кортеж (R, G, B)
        """
        # Получаем границы окна
        rect = RECT()
        self._user32.GetWindowRect(self._hwnd, ctypes.byref(rect))
        self._hdc = self._user32.GetDC(self._hwnd)

        # Рассчитываем координаты пикселя относительно экрана
        screen_x = rect.left + x
        screen_y = rect.top + y

        # Получаем HDC окна

        if not self._hdc:
            raise Exception("Не удалось получить HDC окна")

        # Получаем цвет пикселя
        color = self._gdi32.GetPixel(self._hdc, screen_x, screen_y)
        self._user32.ReleaseDC(self._hwnd, self._hdc)

        if color == -1:  # Проверяем на ошибки
            raise Exception("Ошибка при получении цвета пикселя")

        # Разбираем цвет в RGB
        red = color & 0xFF
        green = (color >> 8) & 0xFF
        blue = (color >> 16) & 0xFF

        return red, green, blue



