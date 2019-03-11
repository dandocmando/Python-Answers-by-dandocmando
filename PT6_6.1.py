import time
import random
import sys



def main():
    print("You are trying to find your way through a maze. You can make 3 choices!")
    answer = input("Make your choice You can go left (L) or right (R) or centre (C) ")

    time.sleep(1)
    if answer == ("R"):
        time.sleep(1)
        print()
        print("A huge arm reaches out of the tunnel and you are never seen again! ")
        time.sleep(1)
        sys.exit()

    elif answer == "L":
        time.sleep(1)
        print()
        print("A spike trap shoots out of the floor and you die! ")
        time.sleep(1)
        sys.exit()

    elif answer == "C":
        time.sleep(1)
        print()
        print("Your have passed level one, Congratulations!")
        time.sleep(1)
        sys.exit()
