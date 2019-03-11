import time

def l():

    print("This program will ask you to input 6 animal names and then ask if you would like the list reversed or not")
    print()
    time.sleep(0.5)
    print("Input 6 animal names")

    arr = input()
    lst = list(map(str,arr.split( )))
    le = len(lst)
    
    lstr = lst[::-1]
    print(lstr)
    print()
    print("Would you like the list reversed or not?")
    yn = input()
    print()
    if yn ==n:
        for le in lst:
            print(le)
            time.sleep(0.5)

    else:
        for le in lstr:
            print(le)
            time.sleep(0.5)
    
    
                 
    
