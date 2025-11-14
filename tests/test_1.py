import pyautogui
import os
import time
import subprocess

import pytest


class TestMyApp:
    @pytest.fixture
    def app(self):
        if os.name == 'nt':
            process = subprocess.Popen([
                r'Z:\APM-964 Регрессия мастера AirViewSetup_8.4.2.12.02c05c4\AirViewSetup_8.4.2.12.02c05c4\AirView.exe'])

        else:
            print('False')

        time.sleep(3)
        yield process
        process.terminate()

    def test_app_opens_correctly(self, app):
        '''Проверка что главное окно открывается'''
        window_title = "AirView 8.4.2.12.02c05c4"
        window_title = pyautogui.locateOnWindow('images/main_window.png', window_title)
        assert window_title is not None, 'Главное окно не найдено'
