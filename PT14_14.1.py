import time

def l():
    print("This program will find the largest number when you provide a group of numbers.")
    time.sleep(1)
    print("Please input a group of numbers with a space between each number:")
    arr = input() # takes the whole line of numbers and puts them on a array/list
    lst = list(map(int,arr.split(' '))) # puts your numbers into a list
    time.sleep(1)
    print("This is your list of numbers:")
    print(lst)
    hgh = max(lst) # max finds highest number in the list
    time.sleep(1)
    print()
    print("The largest number in your list is {0}".format(hgh))
