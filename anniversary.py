import tkinter as Tk
import pyautogui
import time

#configuring the gui and the message so that it can be sized :D
def display_message(message):
    screen_width, screen_height  = pyautogui.size()
    heart_image = pyautogui.image.open('heart.png')

    the_x_position = (screen_width // 2) -200
    the_y_position = (screen_height // 2) -100

    #message now :)

    pyautogui.moveTo(the_x_position, the_y_position)
    pyautogui.typewrite(message, interval= 0.1)

    #sizing of the heart images >:D

    heart_size = 50
    number_of_hearts = 100
    [heart_image.resize((heart_size, heart_size)) for _ in range(number_of_hearts)]

    #the show <3 

    for i in range(number_of_hearts):
        x = int(pyautogui.random.uniform(the_x_position, the_x_position + 400)) #maybe 500? idk
        y = int(pyautogui.random.uniform(the_y_position + 100, screen_height))
        duration = pyautogui.random.uniform(4,5)
        pyautogui.Image(heart_image)

#ladies and gentlemen, the code does not run :)