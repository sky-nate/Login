import random
import os

number = random.randint(1,10)

guess = input("silly game, take a guess from 1 - 10: ")
guess = int(guess)

if guess == number:
    print("yay, you won!")
else:
    os.remove("/home/sky/Vscode/Others")
    print("bye bye!")