import pyautogui
import time
import subprocess


def test_move_mouse():
    process = subprocess.Popen(
        [r'Z:\APM-964 Регрессия мастера AirViewSetup_8.4.2.12.02c05c4\AirViewSetup_8.4.2.12.02c05c4\AirView.exe'])
    time.sleep(3)

    pyautogui.click(109, 36)
    pyautogui.click(131, 59)
    pyautogui.click(882, 360)
    pyautogui.click(1285, 804)
    time.sleep(1)

    process.terminate()
