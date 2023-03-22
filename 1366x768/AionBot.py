from functions import AionBot
import time
from locators import *
import datetime
import pyautogui
from settings import *

bot = AionBot()
last_time = time.time()
iteration_number1 = 1

bot.find_mob_with_down_right_mouse_buttom('right', 5, 0, 1)

pyautogui.sleep(1)
while True:
    if time.time() - last_time < delay_before_search_cycles:
        continue

    bot.save_main_picture('main.png', top=32, left=596, wight=145, height=14)

    if not bot.find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment, 0.98):
        if not bot.find_coordinates_template_img_in_main_img(main_png, full_enemy_heals_bar_fragment, 0.85):

            bot.find_mob_with_down_right_mouse_buttom('right', 58, 0, 1)

        else:
            if only_fight_white_mobs == 'on':
                bot.save_main_picture(determine_enemy, top=27, left=570, wight=8, height=8)
                if bot.find_coordinates_template_img_in_main_img(determine_enemy, determine_enemy_fragment, 0.98):

                    if bot.find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment, 0.98):
                        break

                    start_fight_time = datetime.datetime.today().strftime("%H:%M:%S")
                    start = time.perf_counter()

                    bot.fight_with_error_checking(button_skills, skill_cast_time, button_baf_after_fight, baf_cast_time)

                    end = time.perf_counter()
                    print(f'Fight {iteration_number1} / {start_fight_time} / {round(end - start, 2)} sec')
                    iteration_number1 += 1
                else:
                    pyautogui.press('esc')
            else:
                if bot.find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment, 0.98):
                    break

                start_fight_time = datetime.datetime.today().strftime("%H:%M:%S")
                start = time.perf_counter()

                bot.fight_with_error_checking(button_skills, skill_cast_time, button_baf_after_fight, baf_cast_time)

                end = time.perf_counter()
                print(f'Fight {iteration_number1} / {start_fight_time} / {round(end - start, 2)} sec')
                iteration_number1 += 1
    else:
        bot.looting_dead_mob()
        # pyautogui.press('esc')
        bot.healing_heat_and_mana_point(after_how_many_mod_need_healing)
    last_time = time.time()
