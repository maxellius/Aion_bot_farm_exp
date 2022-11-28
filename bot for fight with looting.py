import time
from random import randint

import cv2 as cv
import mss.tools
import numpy as np
import pyautogui
import datetime


def find_coordinates_template_img_in_main_img(name_img: str, name_tamplate_img: str, resolution: float):
    img_rgb = cv.imread(name_img)
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread(name_tamplate_img, 0)
    w, h = template.shape[::-1]

    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    threshold = resolution
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        x_cord_angle = pt
        y_cord_engle = (pt[0] + w, pt[1] + h)
        x = ((y_cord_engle[0] - x_cord_angle[0]) / 2) + x_cord_angle[0]
        y = ((y_cord_engle[1] - x_cord_angle[1]) / 2) + x_cord_angle[1]
        return x, y


last_time = time.time()

# def exit_check():
#     while True:
#         if keyboard.is_pressed('o'):
#             quit()
#
# thread1 = Thread(target=exit_check)
# thread1.start()

iteration = 1
while True:
    # must be at least 2 seconds before last catch
    if time.time() - last_time < 3:
        continue

    # The screen part to capture
    monitor = {"top": 32, "left": 596, "width": 145, "height": 14}
    output = "main.png".format(**monitor)

    # Grab the data
    sct_img = mss.mss().grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

    print(f'Search {datetime.datetime.today().strftime("%H:%M:%S")}')
    if not find_coordinates_template_img_in_main_img('main.png', '5.png', 0.85):
        if not find_coordinates_template_img_in_main_img('main.png', '7.png', 0.85):

            pyautogui.mouseDown(button='right')
            pyautogui.moveRel(58, 0, 1, _pause=False)

            # pyautogui.keyDown('left')
            # # pyautogui.keyDown('w')
            # time.sleep(0.5)
            # pyautogui.keyUp('left')
            # pyautogui.keyUp('w')
            pyautogui.press('TAB')

        else:
            print(f'Fight {iteration}')
            while find_coordinates_template_img_in_main_img('main.png', '5.png', 0.85) is None:
                if find_coordinates_template_img_in_main_img('main.png', '5.png', 0.85) is not None:
                    break
                pyautogui.press('5')
                if find_coordinates_template_img_in_main_img('main.png', '5.png', 0.85) is not None:
                    break
                pyautogui.press('1')
                if find_coordinates_template_img_in_main_img('main.png', '5.png', 0.85) is not None:
                    break
                pyautogui.press('2')
                if find_coordinates_template_img_in_main_img('main.png', '5.png', 0.85) is not None:
                    break
                pyautogui.press('2')
                if find_coordinates_template_img_in_main_img('main.png', '5.png', 0.85) is not None:
                    break
                pyautogui.press('2')
                if find_coordinates_template_img_in_main_img('main.png', '5.png', 0.85) is not None:
                    break
                pyautogui.press('4')
                if find_coordinates_template_img_in_main_img('main.png', '5.png', 0.85) is not None:
                    break
                pyautogui.press('3')
                if find_coordinates_template_img_in_main_img('main.png', '5.png', 0.85) is not None:
                    break
                pyautogui.press('3')
                sct_img = mss.mss().grab(monitor)
                mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

            # time.sleep(2)
            # pyautogui.press('=')

    # Pick up loot and heal
    else:
        print(f'Lotting {datetime.datetime.today().strftime("%H:%M:%S")}')
        time.sleep(1)
        pyautogui.press('c')
        time.sleep(2)
        pyautogui.keyDown('shift')
        pyautogui.keyDown('c')
        time.sleep(0.5)
        pyautogui.keyUp('shift')
        pyautogui.keyUp('c')
        time.sleep(0.5)
        if iteration % 4 == 0:
            print(f'Healing iteration {iteration}')
            time.sleep(randint(0, 1))
            pyautogui.press('0')
            time.sleep(randint(16, 18))
            pyautogui.press('0')
            time.sleep(randint(0, 1))
        iteration += 1
        last_time = time.time()
