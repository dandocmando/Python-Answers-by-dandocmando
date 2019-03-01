import time

def l():
    print("This program will ask you to input a list of numbers and find the average of those numbers.")
    print()
    time.sleep(1)
    print("Please input your list of numbers with a space in-between each:")
    arr = input()
    lst = list(map(int,arr.split(' ')))
    avg = sum(lst) / float(len(lst))
    print()
    time.sleep(1)
    print("The average of your list of numbers is {0}".format(avg))
