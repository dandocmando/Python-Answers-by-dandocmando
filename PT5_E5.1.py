import time
def main():
    #ask them to put a number in
    print()
    time.sleep(1)
    number = int(input("Please input a number between 1-20: "))

    #your too high
    if number >= 20:
        time.sleep(1)
        print()
        print("Your too high!")

    #your too low
    elif number <1:
        time.sleep(1)
        print()
        print("Your to low!")

    #In the range
    else:
        time.sleep(1)
        print()
        print("Its in the range.")
    
        
        
    
