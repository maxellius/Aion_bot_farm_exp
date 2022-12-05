import time
import cv2 as cv
import mss.tools
import pyautogui
import numpy as np

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

while True:
    # must be at least 2 seconds before last catch
    if time.time() - last_time < 3:
        continue

    monitor = {"top": 114, "left": 332, "width": 9, "height": 9}
    output = "main.png".format(**monitor)

    # Grab the data
    sct_img = mss.mss().grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print('3')
    if find_coordinates_template_img_in_main_img('main.png', 'kolwo.png', 0.3):
        print('1')
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




