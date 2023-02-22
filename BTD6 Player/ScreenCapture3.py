import pyautogui as pg

# Set the time between each line is ran
pg.PAUSE = 1.5

BTD6 = pg.locateOnScreen(r'PicturesforBTD\AppIcon.png', confidence=.8)
# Check if the image was found on the screen
if BTD6 is not None:
    pg.moveTo(BTD6, duration=1.5)
    pg.click(clicks=2, interval=.1)
else:
    print("App not found on screen.")

# Dictionary to map input to image paths
location_dict = {
    'Start': r'PicturesforBTD\StartButton.png',
    'Home': r'PicturesforBTD\HomeButton.png',
    'Settings': r'PicturesforBTD\SettingsButton.png'
}

# Loop to prompt user for input and navigate to location
while True:
    # Prompt user for input
    location_input = input("Where would you like to go? (start/home/settings/close): ")

    # Check if input is valid
    if location_input == 'close':
        print("See you later!")
        break
    elif location_input not in location_dict:
        print("Invalid input. Please try again.")
        continue

    # Get location of image
    location = pg.locateOnScreen(location_dict[location_input], confidence=.8)

    # Check if the image was found on the screen
    if location is not None:
        pg.moveTo(location, duration=1.5)
        pg.click(clicks=2, interval=1.5)
        print(f"You are now on the {location_input} screen!")
    else:
        print("Image not found on screen. Please try again.")