MAX_LINES = 3
def deposit():
    while True:
        lines = input("Eneter the number of lines to be on (1-" + str(MAX_LINES)+ ")?")
        amount = input("how much would you like tp deposit? $ ")
        if lines.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0")

        else:
            print("please enter a number")
            return amount

def get_amount_of_lines ():

def main():
    balance = deposit()


main()

