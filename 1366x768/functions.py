import time
import cv2 as cv
import mss.tools
import numpy as np
import pyautogui
import datetime
from locators import *
from settings import heal_sensitivity


class AionBot():
    def __init__(self):
        self.iteration_number1 = 1
        self.iteration_number2 = 1

    @staticmethod
    def find_coordinates_template_img_in_main_img_RGB(name_main_img: str, name_template_img: str, resolution: float):
        threshold = resolution

        main_img_RGB = cv.imread(name_main_img)
        name_tamplate_img_RGB = cv.imread(name_template_img)

        main_img_R, main_img_G, main_img_B = cv.split(main_img_RGB)
        name_tamplate_img_R, name_tamplate_img_G, name_tamplate_img_B = cv.split(name_tamplate_img_RGB)

        resultB = cv.matchTemplate(main_img_R, name_tamplate_img_R, cv.TM_CCOEFF_NORMED)
        resultG = cv.matchTemplate(main_img_G, name_tamplate_img_G, cv.TM_CCOEFF_NORMED)
        resultR = cv.matchTemplate(main_img_B, name_tamplate_img_B, cv.TM_CCOEFF_NORMED)
        result = resultB + resultG + resultR
        w, h = result.shape[::-1]
        loc = np.where(result >= 3 * threshold)
        for pt in zip(*loc[::-1]):
            x_cord_angle = pt
            y_cord_engle = (pt[0] + w, pt[1] + h)
            x = ((y_cord_engle[0] - x_cord_angle[0]) / 2) + x_cord_angle[0]
            y = ((y_cord_engle[1] - x_cord_angle[1]) / 2) + x_cord_angle[1]
            return x, y

    @staticmethod
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

    @staticmethod
    def save_main_picture(name_picture: str, top: int, left: int, wight: int, height: int):
        monitor = {"top": top, "left": left, "width": wight, "height": height}
        output = name_picture.format(**monitor)

        # Grab the data
        sct_img = mss.mss().grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

    @staticmethod
    def press_shift_c():
        pyautogui.keyDown('shift')
        pyautogui.keyDown('c')
        pyautogui.sleep(0.5)
        pyautogui.keyUp('shift')
        pyautogui.keyUp('c')

    @staticmethod
    def checking_full_bag_or_not():
        AionBot().save_main_picture(chat_png, top=539, left=19, wight=170, height=125)
        if AionBot().find_coordinates_template_img_in_main_img(chat_png, full_bag_fragment,
                                                               0.8):
            for i in range(2):
                pyautogui.press('esc')
            print(f'Bag_is_full {datetime.datetime.today().strftime("%H:%M:%S")}')

    def fight_with_mob_with_waiting(self, buttom_skils: tuple, skill_cast_time: tuple):
        self.iteration_number2 += 1
        a = 0
        for i in buttom_skils:
            if AionBot().find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment,
                                                                   0.98):
                break
            pyautogui.press(i)
            try:
                time.sleep(skill_cast_time[a])
            except IndexError:
                pass
            a += 1

    def baf_after_fight(self, button_baf_after_fight: tuple, baf_cast_time: tuple):
        self.iteration_number2 += 1
        a = 0
        for i in button_baf_after_fight:
            if AionBot().find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment,
                                                                   0.98):
                break
            pyautogui.press(i)
            try:
                time.sleep(baf_cast_time[a])
            except IndexError:
                pass
            a += 1

    @staticmethod
    def looting_dead_mob():
        AionBot().save_main_picture(loot_png, top=134, left=266, wight=10, height=10)
        iteration_number3 = 1
        while AionBot().find_coordinates_template_img_in_main_img(loot_png, './fragments/loot_fragment.png',
                                                                  0.7) is None:
            pyautogui.press('c')
            pyautogui.sleep(1)
            if iteration_number3 % 10 == 0:
                AionBot().save_main_picture(distance_to_loot_1, top=40, left=816, wight=10, height=7)
                pyautogui.sleep(1)
                AionBot().save_main_picture(distance_to_loot_2, top=40, left=816, wight=10, height=7)

                if AionBot().find_coordinates_template_img_in_main_img(distance_to_loot_1, distance_to_loot_2, 0.9):
                    pyautogui.press('esc')
                    break

            AionBot().save_main_picture('main.png', top=32, left=596, wight=145, height=14)
            if AionBot().find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment,
                                                                   0.7) is None:
                break
            iteration_number3 += 1
            AionBot().save_main_picture(loot_png, top=134, left=266, wight=10, height=10)
        else:
            AionBot().press_shift_c()
            AionBot().checking_full_bag_or_not()

    def healing_heat_and_mana_point(self, after_how_many_mod_need_healing: int):
        if self.iteration_number1 % after_how_many_mod_need_healing == 0:

            AionBot().save_main_picture(heal_bar_png, top=711, left=297, wight=141, height=10)
            AionBot().save_main_picture(mana_bar_png, top=725, left=297, wight=141, height=10)

            if AionBot().find_coordinates_template_img_in_main_img(heal_bar_png, heal_bar_fragment,
                                                                   heal_sensitivity) is None or \
                    AionBot().find_coordinates_template_img_in_main_img(mana_bar_png, mana_bar_fragment,
                                                                        heal_sensitivity) is None:
                start = time.perf_counter()
                start_healing_time = datetime.datetime.today().strftime("%H:%M:%S")
                pyautogui.press('0')

                while AionBot().find_coordinates_template_img_in_main_img(heal_bar_png, heal_bar_fragment,
                                                                          heal_sensitivity) is None or \
                        AionBot().find_coordinates_template_img_in_main_img(mana_bar_png, mana_bar_fragment,
                                                                            heal_sensitivity) is None:
                    AionBot().save_main_picture(heal_bar_png, top=711, left=297, wight=141, height=10)
                    AionBot().save_main_picture(mana_bar_png, top=725, left=297, wight=141, height=10)
                else:
                    pyautogui.sleep(0.5)
                    end = time.perf_counter()
                    print(f'Healing {start_healing_time} / {round(end - start, 2)} sec')
                    pyautogui.press('0')

    @staticmethod
    def find_mob_with_down_right_mouse_buttom(buttom: str, x: int, y: int, speed: int):
        pyautogui.mouseDown(button=buttom)
        pyautogui.moveRel(x, y, speed, _pause=True)

        pyautogui.press('TAB')

    # @staticmethod
    # def detect_white_mob():
    #     Aion_bot().save_main_picture(determine_enemy, top=27, left=570, wight=8, height=8)
    #     if Aion_bot().find_coordinates_template_img_in_main_img(determine_enemy, determine_enemy_fragment, 0.98)\
    #             is None:
    #         pyautogui.press('esc')
    #         return

    @staticmethod
    def fight_with_error_checking(button_skills, skill_cast_time, button_baf_after_fight, baf_cast_time):
        AionBot().baf_after_fight(button_baf_after_fight, baf_cast_time)
        iteration_number3 = 1
        while AionBot().find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment, 0.98) \
                is None:
            AionBot().save_main_picture(chat_png, top=539, left=19, wight=170, height=125)
            AionBot().save_main_picture(main_png, top=32, left=596, wight=145, height=14)

            AionBot().fight_with_mob_with_waiting(button_skills, skill_cast_time)

            if iteration_number3 % 3 == 0:
                AionBot().save_main_picture(chat_png, top=539, left=19, wight=170, height=125)
                if AionBot().find_coordinates_template_img_in_main_img(chat_png, error_chat_fragment, 0.9):
                    pyautogui.press('0')
            if iteration_number3 % 8 == 0:
                AionBot().save_main_picture(main_png, top=32, left=596, wight=145, height=14)
                AionBot().save_main_picture(chat_png, top=539, left=19, wight=170, height=125)

                if AionBot().find_coordinates_template_img_in_main_img(chat_png, error2_chat_fragment, 0.9):
                    break

                if AionBot().find_coordinates_template_img_in_main_img(chat_png, error3_chat_fragment, 0.85) or \
                        AionBot().find_coordinates_template_img_in_main_img(main_png,
                                                                            full_enemy_heals_bar_fragment, 0.97):
                    pyautogui.sleep(1)
                    pyautogui.press('esc')
                    break
            AionBot().save_main_picture(main_png, top=32, left=596, wight=145, height=14)

            iteration_number3 += 1
