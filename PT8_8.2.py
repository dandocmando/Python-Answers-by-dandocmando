import statistics
import time

def main():
    print("Please list your numbers leaving a space between each one.")
    print()
    arr = input() # takes the whole line of n numbers and puts them on a array/list
    l = list(map(int,arr.split(' '))) #adds a space between user numbers and maps them into a useable array
    time.sleep(1)
    print()
    print("This is your array of numbers.")
    time.sleep(1)
    print(l)
    avg = float(sum(l))/len(l) #len gets the length of the list and divides it by the sum of the list
    time.sleep(1)
    print()
    print("This is the average of your numbers!")
    time.sleep(1)
    print()
    print(avg)
