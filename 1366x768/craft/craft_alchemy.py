import datetime
import time
import mss.tools
import pyautogui
from functions import AionBot


last_time = time.time()
bot = AionBot()
while True:
    # must be at least 2 seconds before last catch
    if time.time() - last_time < 2:
        continue
    mss.mss().shot(output='full_screen.png')
    bot.save_main_picture('main_up.png', 58, 362, 6, 11)
    bot.save_main_picture('main.png', 114, 332, 9, 9)

    if bot.find_coordinates_template_img_in_main_img('main_up.png', 'up_fragment.png', 0.9):
        try:
            x, y = bot.find_coordinates_template_img_in_main_img('full_screen.png', 'name_fragment.png', 0.65)
            y += 100
            pyautogui.moveTo(x, y, 0.5)
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.press('c')
            time.sleep(0.5)
            pyautogui.moveTo(1210, 225, 0.5)
            pyautogui.click()
            time.sleep(0.5)
            bot.save_main_picture('loot.png', top=322, left=813, wight=10, height=10)
            if bot.find_coordinates_template_img_in_main_img('loot.png', 'loot_fragment.png', 0.7):
                pyautogui.moveTo(713, 438, 0.5)
                pyautogui.click()
        except:
            print('error up')
            continue

    if bot.find_coordinates_template_img_in_main_img('main.png', 'kolwo_fragment.png', 0.3) is None:
        # we take quest at broker
        try:
            x, y = bot.find_coordinates_template_img_in_main_img('full_screen.png', 'name_fragment.png', 0.65)
            y += 100
            pyautogui.moveTo(x, y, 0.5)
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.press('c')
            time.sleep(0.2)
            bot.save_main_picture('button.png', top=250, left=1193, wight=35, height=6)
            if bot.find_coordinates_template_img_in_main_img('button.png', 'button_fragment.png', 0.9):
                pyautogui.moveTo(1210, 252, 0.5)
                pyautogui.click()
        except:
            print('error name')
            continue

        time.sleep(0.5)
        bot.save_main_picture('result.png', 0, 1040, 325, 350)
        if bot.find_coordinates_template_img_in_main_img('result.png', 'quest_icons_fragment.png', 0.85) is None:
            pyautogui.moveTo(1189, 198, 0.5)
            pyautogui.click()
            pyautogui.moveTo(1284, 394, 0.5)
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(0.2)
            bot.save_main_picture('main.png', 114, 332, 9, 9)
            if bot.find_coordinates_template_img_in_main_img('main.png', 'kolwo_fragment.png', 0.3) is None:
                print(f'Resources are over=( {datetime.datetime.today().strftime("%H:%M:%S")}')

        else:
            try:
                x, y = bot.find_coordinates_template_img_in_main_img('result.png', 'quest_icons_fragment.png', 0.9)
                x += 1040
                pyautogui.moveTo(x, y, 0.5)
                pyautogui.click()
                time.sleep(0.5)
                bot.save_main_picture('accept_icons.png', 394, 1264, 35, 4)
            except:
                print('error quest')
                continue
            if bot.find_coordinates_template_img_in_main_img('accept_icons.png', 'accept_icons_fragment.png',
                                                             0.8):
                pyautogui.moveTo(1284, 394, 0.5)
                time.sleep(0.5)
                pyautogui.click()
            else:
                # delete quest
                pyautogui.moveTo(1188, 448, 0.5)
                pyautogui.click()
                pyautogui.moveTo(1137, 752, 0.5)
                pyautogui.click()
                pyautogui.moveTo(738, 418, 0.5)
                pyautogui.click()
    else:
        # craft
        pyautogui.moveTo(203, 117, 0.5)
        time.sleep(0.5)
        pyautogui.click()
        pyautogui.moveTo(346, 450, 0.5)
        time.sleep(0.5)
        pyautogui.click()

        while bot.find_coordinates_template_img_in_main_img('main.png', 'kolwo_fragment.png', 0.3):
            bot.save_main_picture('main.png', 114, 332, 9, 9)
            pass

        else:
            time.sleep(15)
            # we give back quest to broker
            x, y = bot.find_coordinates_template_img_in_main_img('full_screen.png', 'name_fragment.png', 0.65)
            y += 100
            pyautogui.moveTo(x, y, 0.5)
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.press('c')
            time.sleep(0.2)
            bot.save_main_picture('button.png', top=250, left=1193, wight=35, height=6)
            if bot.find_coordinates_template_img_in_main_img('button.png', 'button_fragment.png', 0.95):
                pyautogui.moveTo(1210, 252, 0.5)
                pyautogui.click()

            try:
                time.sleep(0.5)
                bot.save_main_picture('result.png', 0, 1040, 325, 350)
                x, y = bot.find_coordinates_template_img_in_main_img('result.png', 'quest_icons_fragment.png', 0.9)
                x += 1040
                pyautogui.moveTo(x, y, 0.5)
                pyautogui.click()
                time.sleep(0.5)
                bot.save_main_picture('accept_icons.png', 394, 1264, 35, 4)
            except:
                print('error quest')
                continue
            if bot.find_coordinates_template_img_in_main_img('accept_icons.png', 'accept_icons_fragment.png',
                                                             0.8):
                pyautogui.moveTo(1284, 394, 0.5)
                time.sleep(0.5)
                pyautogui.click()
            else:
                # delete quest
                pyautogui.moveTo(1188, 448, 0.5)
                pyautogui.click()
                pyautogui.moveTo(1137, 752, 0.5)
                pyautogui.click()
                pyautogui.moveTo(738, 418, 0.5)
                pyautogui.click()

    last_time = time.time()




