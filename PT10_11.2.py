import time

def l():
    print("This program makes a multiplication table from your specified number.")
    time.sleep(1)
    print("Choose a number:")
    lst = int(input())
    time.sleep(1)
    print("Your multiplication table:")
    print()
    time.sleep(0.5)
    for i in range(1,13):
        time.sleep(0.25)
        print(lst,'x',i,'=',lst*i)
