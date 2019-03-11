import time

def l():

    print("This program will ask you to input 6 animal names and then ask if you would like the list reversed or not")
    print()
    time.sleep(0.5)
    print("Input 6 animal names")

    arr = input()
    lst = list(map(str,arr.split( )))
    le = len(lst)
    
    lstr = lst.reverse()
    print(lstr)
    print()
    print("Would you like the list reversed or not?")
    print()
    
    
    for le in lst:
        print(le)
        time.sleep(0.5)
                 
    
