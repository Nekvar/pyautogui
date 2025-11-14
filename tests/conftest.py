import pytest
import pyautogui
import platform
import subprocess
import time


def pytest_addoption(parser):
    parser.addoption("--os", action="store", default=platform.system().lower())


@pytest.fixture
def screens_dir(request):
    """Определяем папку со скриншотами для текущей ОС"""
    os_name = request.config.getoption("--os")
    return f"images/{os_name}/"


@pytest.fixture
def app_controller():
    """Управление приложением"""

    class AppController:
        def __init__(self):
            self.process = None

        def start_app(self):
            if platform.system() == "Windows":
                self.process = subprocess.Popen([r"app.exe"])
            else:
                self.process = subprocess.Popen(["./app"])
            time.sleep(3)

        def close_app(self):
            if self.process:
                pyautogui.hotkey('alt', 'f4')  # Универсальное закрытие
                time.sleep(1)
                self.process.terminate()

    controller = AppController()
    controller.start_app()
    yield controller
    controller.close_app()