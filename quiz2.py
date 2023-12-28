#still needs a couple of debugging to do...
name = input("Hello user, what is your name? ")
print(f"Hello {name} welcome to my quiz, have fun!")

start = input("do you want to play? Y/N: ")
if start == "Yes" or "yes" or "y":
    print("Great, lets get started!")
    points = 0

print('''Question 1: What is the capital of France?
A) Berlin
B) Madrid
C) Paris
D) Rome''')

q1 = input("what is the answer? ")
if q1 == "c":
    print("correct!")
    print(f"you have {points+1} point(s) so far!")
    points = 1
    print("-------------------------------------------------------")
else:
    print("incorrect! its C")
    print(f"you now have {points-1} points")
    print("-------------------------------------------------------")
    points = -1

print('''Question 2: What is known as the Red planet?
A) Venus
B) Mars
C) Jupiter
D) Saturn''')

q2 = input("what is the answer? ")
if q2 == "A" or "a":
    print("correct!")
    print(f"you have {points + 1} points so far. Rock on dude")
    points = 2
    print("-------------------------------------------------------")
else:
    print("incorrect! its A")
    print(f"you now have {points -1} points. You got this")
    print("-------------------------------------------------------")

print('''Question 3: Who wrote the play "Romeo & Juliet"?
A) Charles Dickens
B) William Shakespeare
C) Jane Austen
D) Mark Twain''')

q3 = input("what is the answer? ")
if q3 == "b" or "B":
    print("correct!")
    print(f"you now have {points + 1} points. Nice one!")
    print("-------------------------------------------------------")

else:
    print("incorrect! its B")
    print(f"you now have {points -1} points. Tough one I know")
    print("-------------------------------------------------------")

print('''Question 4: What is the symbol of Gold?
A) Gd
B) Au
C) Ag
D) Fe''')

q4 = input("what is the answer? ")
if q4 == "B" or "b":
    print("correct")
    print(f"you now have {points + 2} points. On a roll wow")
    print("-------------------------------------------------------")
else:
    print("incorrect! its B")
    print(f"you now have {points -1} points. Uh oh")
    print("-------------------------------------------------------")


print('''Question 5: What is a primary color here?
A) Orange
B) Green
C) Red
D) Purple''')

q5 = input("what is the answer? ")
if q5 == "C" or "c":
    print("correct!")
    print(f"you have {points + 3} points. Yessir")
    print("-------------------------------------------------------")

else:
    print("incorrect! its C")
    print(f"you now have {points - 1} points. Stand up soldier")
    print("-------------------------------------------------------")

print('''Question 6: In which year did Christopher Columbus first reach the Americas?
A) 1492
B) 1588
C) 1776
D) 1804''')

q6 = input("whats the answer? ")
if q6 == "A" or "a":
    print("Correct!")
    print(f"you have {points + 4} points. Congrats {name}!")
    print("-------------------------------------------------------")

else:
    print("incorrect! its A")
    print(f"you now have {points -1} points. Pick it up!")
    print("-------------------------------------------------------")

print('''Question 7: What is the largest ocean?
A) Atlantic Ocean
B) Indian Ocean
C) Pacific Ocean
D) Southern Ocean''')

q7 = input("what is the answer? ")
if q7 == "C" or "c":
    print("correct!")
    print(f"you have {points + 5} points. Keep it up {name}")
    print("-------------------------------------------------------")

else:
    print("incorrect! it was C")
    print(f'you now have {points - 1} points. Oh no amigo')
    print("-------------------------------------------------------")

print('''Question 8: Who is the author of Harry Potter?
 A) J.K. Rowling
B) George R.R. Martin
C) Stephen King
D) J.R.R. Tolkien''')

q8 = input("whats the answer? ")
if q8 == "A" or "a":
    print("correct!")
    print(f"you have {points +6 } points. Wow {name} nice one!")
    print("-------------------------------------------------------")

else:
    print("incorrect! it was A")
    print(f"you now have {points - 1} points. Get em {name}!")
    print("-------------------------------------------------------")


print('''Question 9: What is the powerhouse of the cell?
A) Nucleus
B) Mitochondria
C) Endoplasmic reticulum
D) Golgi apparatus''')

q9 = input("whats the answer? ")
if q9 == "B" or "b":
    print("correct!")
    print(f"you have {points + 7} points. I am proud of you")
    print("-------------------------------------------------------")
else:
    print("incorrect! it was B")
    print(f"you now have {points - 1} points. Well... its okay, the next one for sure")
    print("-------------------------------------------------------")

print('''Question 10: What is an example of a renewable resource?
A) Coal
B) Natural Gas
C) Solar
D) Nuclear''')

q10 = input("what is the answer? ")

if q10 == "B" or "b":
    print("correct!")
    print(f"you have {points + 8} points. wow {name} great job!")
    print("-------------------------------------------------------")

else:
    print("incorrect! it was B")
    print(f"you now have {points - 1} points, you fought well {name} see ya soon.")
    print("-------------------------------------------------------")

end = input("Want to play again? Y/N ")
if end == "Yes" or "Y" or "y":
    print(True)

else:
    print("Bye bye")
    quit