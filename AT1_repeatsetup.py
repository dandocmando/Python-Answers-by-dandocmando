import time
import random

def l():
    qsq = ["A way of farming that combines agriculture and business and usually involves large amounts of land, animals, and expensive technology is?",
           "A. Agriculture","B. Agribusiness","C. Farming"]
    qs2 = ["test"]
    lst = [qsq,qs2]
    
    ss = 0
    at = 0
    chc = "You have 3 Chances."
    qst = "The first question is:"
    print("This program will ask you the question 3 times and then give you a score")
    print(qsq[0])
    print(qsq[1])
    print(qsq[2])
    print()
    print(qst)
    test = random.choice(lst)
    print(test)
    print()
    print()
    print()


    print()
    print(chc)
    print()
    rslt = input()
    while rslt != "B".lower() and at<1:
        if at ==0:
            print("You have 2 more chances!")
        if at ==1:
            print("You have 1 more chances!")
        at = at + 1
        rslt = input()
    print(at)  
    if at == 1:
        at = 0
        print("The answer to the question is B. Agribusiness")
        print("Your score is {0} so far.".format(ss))
    elif at < 3:
        at = 0
        print("Correct, the Answer was B. Agribusiness")
        ss = ss + 1
        print("Your score is {0} so far".format(ss))

    print("The second question is:")
    print("To gather a crop when it is finished growing is called?")
    print()

    print("A. Collect")
    print("B. Gather")
    print("C. Harvest")

    print()
    print(chc)
    print()
    while rslt != "C".lower() and at<1:
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
    
    

    


