import time
def l():
    count = 10
    print("This program counts down from 10 in second intervals.")
    print()
    time.sleep(1)
    for count in reversed(range(1, count+1)):
        time.sleep(1)
        print("You have {0} seconds left.".format(count))
    time.sleep(1)
    print()
    print("CountDown has finished!")
