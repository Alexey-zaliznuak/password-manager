from pyautogui import size, moveTo, click, position
from keyboard import is_pressed
from random import randint

width, heigth = size()

while not is_pressed("Esc"):
    moveTo(randint(0, width), randint(0, heigth), 0.1)
    click(position())