import pyautogui as pg

# Sets the time between each line is ran
pg.PAUSE = 1.5

Path = r'PicturesforBTD\StartButton.png'
Path2 = r'PicturesforBTD\HomeScreen.png'

location = pg.locateOnScreen(Path, confidence=.8)
location2 = pg.locateOnScreen(Path2, confidence=.8)

# Check if the image was found on the screen
if location is not None:
    pg.moveTo(location, duration=1.5)
    pg.leftClick()
else:
    print("Image not found on screen.")

# Check if the image was found on the screen
if location2 is not None:
    pg.moveTo(location2, duration=1.5)
    print("You are on the homescreen!")
else:
    print("Image not found on screen.")
