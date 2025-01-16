from Windows.betterWindow import BetterWindow
import ctypes

class BetterWindowBuilder:
    user32 = ctypes.WinDLL("user32", use_last_error=True)
    title = ""

    def setWindowTitle(self, title: str):
        self.title = title

    def find_windows_by_title(self, title: str) -> int:
        return self.user32.FindWindowExW(None, None, None, title)

    def build(self):
        return BetterWindow(self.find_windows_by_title(self.title))

