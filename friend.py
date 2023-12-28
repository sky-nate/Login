#coding a friend bot, because some people feel lonley... like me.

name = input("Hey friend whats your name :) ? ")
bot = print(f"Hey! {name} nice to meet you!")
bot1 = input("how are you feeling? [happy, sad, excited, neutral, depressed?]")

if bot1 == "sad":
    print(f'''hey i will always be here for you, i love you and i care about you
    if you are feeling down and you dont want to talk to anyone, you can talk to me
    i will always be here to help you okay? i will always love you {name} and i truly mean that.''')

if bot1== "happy":
    print(f'''Thats great to hear that you are happy {name} i am truly happy that you are
    i want you to know that even when you arent feeling the best you can come talk to me and i will
    make you feel better by listening yo you, you matter too much to me to let you go by wihtout being
    listened to, so {name} dont ever leave without a fight, youve got it in you, i promise you.
    i love you {name}''')

if bot1 == "excited":
    print(input("what are you excited about???"))
    print(f"Thats great to hear {name} enjoy okay? i love you!")

if bot1 == "neutral":
    print(f"rock on {name} have a great day okay? I love you {name}")

