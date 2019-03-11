import time

def main():
    lives = 3
    correct = 0
    print("This is a quiz on farming...")
    print()
    print("Score = {0}".format(correct))
    print("You have {0} lives".format(lives))
    print()
    print("Question 1 ")
    print("What percentage of the land is used for farming?")
    print()
    print("a. 25%")
    print("b. 50%")
    print("c. 75%")
    print("d. 99%")
    
    answer  = input("make your choice: ")
    if answer == "c":
        correct = correct+1
        print("fuck your right!")
        print("Score = {0}".format(correct))
    elif answer =="a":
        print("Fuck your wrong")
    elif answer =="b":
        lives = lives-1
        print("incorrect try again")
        print(lives)
    elif answer =="d":
        print("Your mentally retarded")
    
    
