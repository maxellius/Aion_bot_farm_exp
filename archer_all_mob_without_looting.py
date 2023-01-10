from functions import AionBot
import time
from locators import *
import datetime
import pyautogui

bot = AionBot()
last_time = time.time()
iteration_number1 = 1

bot.find_mob_with_down_right_mouse_buttom('right', 5, 0, 1)

time.sleep(1)
while True:
    if time.time() - last_time < 2:
        continue

    bot.save_main_picture('main.png', top=32, left=596, wight=145, height=14)

    if not bot.find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment, 0.98):
        if not bot.find_coordinates_template_img_in_main_img(main_png, full_enemy_heals_bar_fragment, 0.85):

            bot.find_mob_with_down_right_mouse_buttom('right', 58, 0, 1)

        else:
            if bot.find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment, 0.98):
                break

            start_fight_time = datetime.datetime.today().strftime("%H:%M:%S")
            start = time.perf_counter()

            bot.baf_after_fight('7', '8', '9')
            iteration_number3 = 1
            while bot.find_coordinates_template_img_in_main_img(main_png, empty_enemy_heals_bar_fragment, 0.98) \
                    is None:
                bot.save_main_picture(chat_png, top=539, left=19, wight=170, height=125)
                bot.save_main_picture(main_png, top=32, left=596, wight=145, height=14)

                bot.fight_with_mob('5', '1', '2', '2', '2', '4', '3', '3', '6')

                if iteration_number3 % 3 == 0:
                    bot.save_main_picture(chat_png, top=539, left=19, wight=170, height=125)
                    if bot.find_coordinates_template_img_in_main_img(chat_png, error_chat_fragment,
                                                                     0.85):
                        pyautogui.press('0')
                if iteration_number3 % 6 == 0:
                    bot.save_main_picture(main_png, top=32, left=596, wight=145, height=14)
                    bot.save_main_picture(chat_png, top=539, left=19, wight=170, height=125)

                    if bot.find_coordinates_template_img_in_main_img(chat_png, error2_chat_fragment,
                                                                     0.85):
                        break

                    if bot.find_coordinates_template_img_in_main_img(chat_png, error3_chat_fragment, 0.85) or \
                            bot.find_coordinates_template_img_in_main_img(main_png, full_enemy_heals_bar_fragment,
                                                                          0.97):
                        time.sleep(1)
                        pyautogui.press('esc')
                        break
                bot.save_main_picture(main_png, top=32, left=596, wight=145, height=14)

                iteration_number3 += 1
            end = time.perf_counter()
            print(f'Fight {iteration_number1} / {start_fight_time} / {round(end - start, 2)} sec')
            iteration_number1 += 1


    else:
        # bot.looting_dead_mob()
        pyautogui.press('esc')
        bot.healing_heat_and_mana_point(1)
    last_time = time.time()
