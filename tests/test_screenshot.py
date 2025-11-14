import pyautogui
import os
import time
import subprocess
import pytest
from datetime import datetime
import sys

# class TestMyApp:
#    @pytest.fixture
#    def app(self):
#        if os.name == 'nt':
#            process = subprocess.Popen([
#                r'Z:\APM-964 Регрессия мастера AirViewSetup_8.4.2.12.02c05c4\AirViewSetup_8.4.2.12.02c05c4\AirView.exe'])
#
#        else:
#            print('False')
#
#        time.sleep(3)
#        yield process
#        process.terminate()
#
#    def test_app_opens_correctly(self, app):
#        '''Проверка что главное окно открывается'''
#        window_title = "AirView 8.4.2.12.02c05c4"
#        window_title = pyautogui.locateOnWindow('images/main_window.png', window_title)
#        assert window_title is not None, 'Главное окно не найдено'


def test_complete_screenshot():
    process = subprocess.Popen(
        [r'Z:\APM-964 Регрессия мастера AirViewSetup_8.4.2.12.02c05c4\AirViewSetup_8.4.2.12.02c05c4\AirView.exe'])
    time.sleep(3)


    screenshot = pyautogui.screenshot()
    timestamp = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
    screenshot.save(f'../images/windows/{timestamp}.png')

    process.terminate()

