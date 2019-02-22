import time

def l():
    print("This program checks that a given character is in a given string")
    print()
    time.sleep(1)
    print("Input a String:")
    string = input()
    print()
    time.sleep(1)
    print("Input a Character:")
    character = input()
    time.sleep(1)
    if character in string:
        print()
        print("Found!")
    else:
        print()
        print("Not found!")
