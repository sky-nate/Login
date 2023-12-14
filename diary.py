import datetime

def write_entry(date, entry):
    with open("The diary.txt","a") as f:
        f.write(date + "\n")
        f.write(entry +"\n")
        f.write("------------------------------------------\n")

def read_enrties():
    with open("The diary.txt", "r") as f:
        entries = f.read()
        print(entries)


def main():
    while True:
        print("1. Document an entry")
        print("2. You can read your entries")
        print("3. End")
        choice = input("choose an option 1-3: ")

        if choice == "1":
            date = datetime.datetime.now().strftime("%Y-%M-%d %H:%M:%S")
            entry = input("Type entry here... ")
            write_entry(date, entry)
            print("Entry has been written down!")

        elif choice == "2":
            print("all your entries: ")
            read_enrties()

        elif choice == "3":
            print("have a great day!")

        else:
            print("your choice was invalid, please try again... ")

if __name__ == "__main__":
    main()