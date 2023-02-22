import os
import time

import pyautogui as pg

# Sets the time between each line is ran
pg.PAUSE = 4

# Define paths to images
start_button_path = r'PicturesforBTD\StartButton.png'
heroes_path = r'PicturesforBTD\Heroes\Heroes.png'
admiral_brickell_path = r'PicturesforBTD\Heroes\AdmiralBrickell.png'
select_button_path = r'PicturesforBTD\Heroes\SelectButton.png'
back_button_path = r'PicturesforBTD\BackButton.png'
play_button_path = r'PicturesforBTD\HomePage\PlaySolo.png'
easy_map_path = r'PicturesforBTD\MapSelection\EasySelection.png'
standard_path = r'PicturesforBTD\MapSelection\Standard.png'
monkey_meadows_path = r'PicturesforBTD\MapSelection\MonkeyMeadows.png'
main_menu_path = r'PicturesforBTD\HomePage\MainMenu.png'

# Check if game is already open
main_menu_location = pg.locateOnScreen(main_menu_path, confidence=.8)
if main_menu_location is not None:
    print("Game is already open.")
else:
    # Navigate to the desktop and open the game
    os.startfile(r'C:\Program Files (x86)\Steam\steamapps\common\BloonsTD6\BloonsTD6.exe')
    time.sleep(15)  # Wait for game to load

    # Navigate through the Start button screen to reach the homepage
    start_button_location = pg.locateOnScreen(start_button_path, confidence=.8)
    if start_button_location is not None:
        pg.moveTo(start_button_location, duration=1.5)
        pg.doubleClick()  # Double-click to continue through the Start button screen
    else:
        print("Start button not found on screen.")
        exit()

    # Select Admiral Brickell hero
    heroes_location = pg.locateOnScreen(heroes_path, confidence=.8)
    if heroes_location is not None:
        pg.moveTo(heroes_location, duration=1.5)
        pg.click()  # Click to open heroes menu
        admiral_brickell_location = pg.locateOnScreen(admiral_brickell_path, confidence=.8)
        if admiral_brickell_location is not None:
            pg.moveTo(admiral_brickell_location, duration=1.5)
            pg.click()  # Click to select Admiral Brickell hero
            select_button_location = pg.locateOnScreen(select_button_path, confidence=.8)
            if select_button_location is not None:
                pg.moveTo(select_button_location, duration=1.5)
                pg.click()  # Click to confirm hero selection
                back_button_location = pg.locateOnScreen(back_button_path, confidence=.8)
                if back_button_location is not None:
                    pg.moveTo(back_button_location, duration=1.5)
                    pg.click()  # Click to navigate back to the main menu
                else:
                    print("Back button not found on screen.")
                    exit()
            else:
                print("Select button not found on screen.")
                exit()
        else:
            print("Admiral Brickell not found on screen.")
            exit()
    else:
        print("Heroes not found on screen.")
        exit()
            # Click on "Standard" button
    standard_button_location = pg.locateOnScreen(standard_path, confidence=.8)
    if standard_button_location is not None:
        pg.moveTo(standard_button_location, duration=1.5)
        pg.click()
    else:
        print("Standard button not found on screen.")
        exit()

    # Click on "Monkey Meadows" button
    monkey_meadows_location = pg.locateOnScreen(monkey_meadows_path, confidence=.8)
    if monkey_meadows_location is not None:
        pg.moveTo(monkey_meadows_location, duration=1.5)
        pg.click()
    else:
        print("Monkey Meadows not found on screen.")
        exit()

    # Click on "Easy" button
    easy_map_location = pg.locateOnScreen(easy_map_path, confidence=.8)
    if easy_map_location is not None:
        pg.moveTo(easy_map_location, duration=1.5)
        pg.click()
    else:
        print("Easy map not found on screen.")
        exit()
