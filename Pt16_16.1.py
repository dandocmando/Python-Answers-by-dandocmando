import time

def l():

    print("This program will ask you to input 6 animal names and then ask if you would like the list reversed or not.")
    print()
    time.sleep(0.5)
    print("Input 6 animal names:")

    arr = input()
    lst = list(map(str,arr.split( )))
    le = len(lst)
    if le < 6:
        print("You haven't entered 6 animals yet, please add {0} more!".format(6-le))
        arr2 = input()
        lst2 = list(map(str,arr2.split( )))
        lst.extend(lst2)

    lstr = lst[::-1]
    print()
    print("Would you like the list reversed or not?")
    yn = input()
    print()
    if yn == 'no':
        print("This is your list:")
        for le in lst:
            print(le)
            time.sleep(0.5)

    elif yn =="yes":
        print('This is your list reversed:')
        for le in lstr:
            print(le)
            time.sleep(0.5)

    else:
        print("You didn't select either option, so here is both:")
        print()
        print("Normal list:")
        for le in lst:
            print(le)
            time.sleep(0.5)
        print()
        print("Reversed list:")
        for le in lstr:
            print(le)
            time.sleep(0.5)
