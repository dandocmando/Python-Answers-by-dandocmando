import time

def l():
    print("This program will tell you the season from the current month.")

    print("Please enter the month:")
    mn = int(input())
    print()

    if mn in (1,2,12):
        print("This month is in Summer!")

    elif mn in (3,4,5):
        print("This month is in Autumn!")

    elif mn in (6,7,8):
        print("This month is in Winter!")

    elif mn in (9,10,11):
        print("This month is in Spring!")

    else:
        print("Don't you know we only have 12 months?")
