import time
import random

def l():
    print("This program will ask you for a list of animals and then tell where the animal is in the list")
    time.sleep(0.5)
    print("Please type a list of animals with a space inbetween each")
    
    arr = input()
    print()
    lst = list(map(str,arr.split( )))
    time.sleep(0.5)
    le = len(lst)
    time.sleep(0.5)
    print("You have {0} items in your animal list.".format(le))
    print()
    time.sleep(0.5)
    for counter in range(le):
        time.sleep(0.5)
        print("Animal {0} is {1}".format((counter+1),lst[counter]))
    
    
