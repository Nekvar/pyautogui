import pyautogui
import time
import subprocess
from datetime import datetime


def test_complete_screenshot():
    process = subprocess.Popen(
        [r'Z:\APM-964 Регрессия мастера AirViewSetup_8.4.2.12.02c05c4\AirViewSetup_8.4.2.12.02c05c4\AirView.exe'])
    time.sleep(3)

    screenshot = pyautogui.screenshot()
    timestamp = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
    screenshot.save(f'../images/windows/{timestamp}.png')

    process.terminate()
