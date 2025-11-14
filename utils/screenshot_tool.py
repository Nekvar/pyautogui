import pyautogui
import os

def capture_ui_elements():
    """Утилита для создания скриншотов элементов UI"""
    print("Подготовьте приложение и нажмите Enter для создания скриншотов...")
    input()

    elements = {
        'main_window': "Скриншот главного окна",
        'start_button': "Кнопка Запуск",
        'calculate_btn': "Кнопка Расчет",
        'result_field': "Поле результата"
    }

    os.makedirs("images", exist_ok=True)

    for name, description in elements.items():
        print(f"Подготовьте: {description} и нажмите Enter")
        input()

        # Определяем область для скриншота
        print("Кликните в левый верхний угол элемента...")
        # Здесь можно добавить определение координат
        screenshot = pyautogui.screenshot()
        screenshot.save(f"images/{name}.png")
        print(f"Сохранено: images/{name}.png")