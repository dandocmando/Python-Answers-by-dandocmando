import time

def l():
    print("This program will tell you how many points each football team scored based on the result")
    time.sleep(0.5)
    print("Enter the name of team one:")
    t1 = input()
    print()
    time.sleep(0.5)
    print("Enter the name of team two:")
    t2 = input()
    print()
    time.sleep(0.5)
    print("Enter the score for {0}: ".format(t1))
    t1Score = input()
    print()
    time.sleep(0.5)
    print()
    print("Enter the score for {0}: ".format(t2))
    t2Score = input()
    print()
    time.sleep(0.5)

    if t1Score > t2Score:
        print("{0} scored {1} and {2} scored {3}".format(t1,t1Score,t2,t2Score))
        print()
        time.sleep(1)
        print("{0} wins!".format(t1))
    elif t1Score < t2Score:
        print("{0} scored {1} and {2} scored {3}".format(t2,t2Score,t1,t1Score))
        print()
        print("{0} wins!".format(t2))
    else:
        print("Both {0} and {1} score 1 points.".format(t1,t2))
        print()
        time.sleep(1)
        print("Its a draw!")
