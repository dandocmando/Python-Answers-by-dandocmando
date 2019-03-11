import time

def l():
    lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    print("This program will tell you the season from the current month.")
    print()
    print("")
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

    if mn == 2:
        print()
        print("There are 28 days in {0}.".format(lst[mn-1]))

    elif mn in (4,6,9,11):
        print()
        print("There are 30 days in {0}.".format(lst[mn-1]))

    elif mn in (1,3,5,7,8,10):
        print()
        print("There are 31 days in {0}.".format(lst[mn-1]))
