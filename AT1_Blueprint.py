import time

def l():
    ss = 0
    at = 0
    print("This program will ask you the question 3 times and then give you a score")
    print("You have 3 Chances.")
    rslt = input()
    while rslt != "B" and at<1:
        if at ==0:
            print("You have 2 more chances!")
        if at ==1:
            print("You have 1 more chances!")
        at = at + 1
        rslt = input()
        
    print(at)  
    if at == 2:
        at = 0
        print("Incorrect")
        print
    elif at < 3:
        at = 0
        print("Correct")
        ss = ss + 1
        print(ss)


    


