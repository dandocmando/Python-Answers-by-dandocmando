import re
import time

def l():
    print("This program will ask your for a list of words and then find all words starting with s.")
    print()
    time.sleep(1)
    print("Please input your list of letters:")
    rslt = input()
    print()
    arr = rslt # takes the whole line of n numbers and puts them on a array/list
    ls = list(map(str,arr.split(' '))) # puts words into a formatted list
    sfind = re.findall (r'\b[s]\w+', rslt) #searches the list for all words starting with s
    time.sleep(1)
    print("This is the total list:")
    print(ls)
    print()
    time.sleep(1)
    print("This is all the words starting with s:")
    print(sfind)
    print()
    time.sleep(1)
    print("This is the amount of words in the total list:")
    print(len(ls))
    print()
    time.sleep(1)
    print("This is the amount of words starting with s:")
    print(len(sfind))
