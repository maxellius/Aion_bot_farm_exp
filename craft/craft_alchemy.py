import time
import cv2 as cv
import mss.tools
import pyautogui
import numpy as np
from functions import AionBot


last_time = time.time()
bot = AionBot()
while True:
    # must be at least 2 seconds before last catch
    if time.time() - last_time < 3:
        continue
    bot.save_main_picture('main.png', 114, 332, 9, 9)
    if bot.find_coordinates_template_img_in_main_img('main.png', 'kolwo.png', 0.3):
        # craft
        pyautogui.moveTo(203, 117, 0.5, _pause=False)
        time.sleep(0.5)
        pyautogui.click()
        pyautogui.moveTo(346, 450, 0.5, _pause=False)
        time.sleep(0.5)
        pyautogui.click()

    else:
        time.sleep(15)
        print('2')
        # broker
        pyautogui.moveTo(1011, 245, 0.5, _pause=False)
        pyautogui.click()
        pyautogui.click()
        pyautogui.moveTo(1210, 252, 0.5, _pause=False)
        pyautogui.click()
        pyautogui.moveTo(1189, 172, 0.5, _pause=False)
        pyautogui.click()
        pyautogui.moveTo(1284, 394, 0.5, _pause=False)
        time.sleep(0.5)
        pyautogui.click()
        # pyautogui.mouseDown(button='left')
        # time.sleep(0.5)
        # pyautogui.mouseUp(button='left')

        pyautogui.moveTo(1011, 245, 0.5, _pause=False)
        pyautogui.click()
        pyautogui.click()
        pyautogui.moveTo(1210, 252, 0.5, _pause=False)
        pyautogui.click()
        pyautogui.moveTo(1189, 172, 0.5, _pause=False)
        pyautogui.click()
        pyautogui.moveTo(1284, 394, 0.5, _pause=False)
        time.sleep(0.5)
        pyautogui.click()
        # pyautogui.mouseDown(button='left')
        # time.sleep(0.5)
        # pyautogui.mouseUp(button='left')
        last_time = time.time()




