import time
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


def save_main_picture(name_picture: str, top: int, left: int, wight: int, height: int):
    monitor = {"top": top, "left": left, "width": wight, "height": height}
    output = name_picture.format(**monitor)

    # Grab the data
    sct_img = mss.mss().grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)


last_time = time.time()

main_png = 'main.png'
chat_png = 'chat.png'
loot_png = 'loot.png'
empty_enemy_heals_bar_fragment = './fragments/empty_heals_bar_fragment.png'
heal_bar_png = 'heal.png'
heal_bar_fragment = './fragments/heal_fragment.png'
distance_to_loot_1 = 'distance_to_loot_1.png'
distance_to_loot_2 = 'distance_to_loot_2.png'
error_chat_fragment = './fragments/error_chat_fragment.png'

iteration = 1
while True:
    # must be at least 2 seconds before last catch
    if time.time() - last_time < 3:
        continue

    save_main_picture('main.png', top=32, left=596, wight=145, height=14)

    print(f'Search {datetime.datetime.today().strftime("%H:%M:%S")}')
    if not find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment, 0.98):
        if not find_coordinates_template_img_in_main_img(main_png, './fragments/full_enemy_heal_bar.png', 0.85):

            pyautogui.mouseDown(button='right')
            pyautogui.moveRel(58, 0, 1, _pause=True)

            pyautogui.press('TAB')

        else:
            print(f'Fight _{iteration}_ {datetime.datetime.today().strftime("%H:%M:%S")}')
            if find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment, 0.98) is not None:
                break
            pyautogui.press('7')
            time.sleep(1)
            if find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment, 0.98) is not None:
                break
            pyautogui.press('8')
            time.sleep(1)
            if find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment, 0.98) is not None:
                break
            pyautogui.press('9')
            while find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment, 0.98) is None:
                if find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment,
                                                             0.98) is not None:
                    break
                pyautogui.press('5')
                if find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment,
                                                             0.98) is not None:
                    break
                pyautogui.press('1')
                if find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment,
                                                             0.98) is not None:
                    break
                pyautogui.press('2')
                if find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment,
                                                             0.98) is not None:
                    break
                pyautogui.press('2')
                if find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment,
                                                             0.98) is not None:
                    break
                pyautogui.press('2')
                if find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment,
                                                             0.98) is not None:
                    break
                pyautogui.press('4')
                if find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment,
                                                             0.98) is not None:
                    break
                pyautogui.press('3')
                if find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment,
                                                             0.98) is not None:
                    break
                pyautogui.press('3')
                if find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment,
                                                             0.98) is not None:
                    break
                pyautogui.press('6')
                save_main_picture(chat_png, top=539, left=19, wight=170, height=125)
                if find_coordinates_template_img_in_main_img(chat_png, error_chat_fragment,
                                                             0.9) is not None:
                    pyautogui.press('0')
                save_main_picture(main_png, top=32, left=596, wight=145, height=14)


    else:
        # print(f'Lotting {datetime.datetime.today().strftime("%H:%M:%S")}')
        # save_main_picture(loot_png, top=134, left=266, wight=10, height=10)
        # a = 1
        # while find_coordinates_template_img_in_main_img(loot_png, './fragments/loot_fragment.png', 0.7) is None:
        #     time.sleep(0.5)
        #     pyautogui.press('c')
        #     time.sleep(1)
        #     if a % 10 == 0:
        #         save_main_picture(distance_to_loot_1, top=40, left=816, wight=10, height=7)
        #         time.sleep(1)
        #         save_main_picture(distance_to_loot_2, top=40, left=816, wight=10, height=7)
        #
        #         if find_coordinates_template_img_in_main_img(distance_to_loot_1, distance_to_loot_2, 0.9):
        #             pyautogui.press('esc')
        #             break
        #
        #     save_main_picture('main.png', top=32, left=596, wight=145, height=14)
        #     if find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment,
        #                                                  0.7) is None:
        #         break
        #     a += 1
        #     save_main_picture(loot_png, top=134, left=266, wight=10, height=10)
        # else:
        #     pyautogui.keyDown('shift')
        #     pyautogui.keyDown('c')
        #     time.sleep(0.5)
        #     pyautogui.keyUp('shift')
        #     pyautogui.keyUp('c')
        print(f'Healing {datetime.datetime.today().strftime("%H:%M:%S")}')
        # pyautogui.press('esc')
        save_main_picture(heal_bar_png, top=711, left=297, wight=141, height=10)
        if find_coordinates_template_img_in_main_img(heal_bar_png, heal_bar_fragment, 0.66) is None:
            time.sleep(0.5)
            pyautogui.press('0')
            while find_coordinates_template_img_in_main_img(heal_bar_png, heal_bar_fragment, 0.66) is None:
                save_main_picture(heal_bar_png, top=711, left=297, wight=141, height=10)
            else:
                time.sleep(0.5)
                pyautogui.press('0')
        iteration += 1
        last_time = time.time()
