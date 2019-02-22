import time

def l():
    i_min = int(1)
    print("This program squares all the numbers between you specified number and 1")
    print("Choose a number: ")
    print()
    time.sleep(1)
    i_max = int(input())
    lst =list(range(i_min, i_max +1)) #formats numbers into a readable list
    print("This is your list of numbers to be squared")
    time.sleep(1)
    print(lst)
    print()
    for i in lst:
        time.sleep(1)
        print("{0} squared is {1}.".format(i,i*i))
