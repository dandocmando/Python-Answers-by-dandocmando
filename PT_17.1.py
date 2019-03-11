import time

def l():
    print("This program will ask you for the items you need on your shopping list.")
    time.sleep(0.5)
    print("Please type the items you want on your shopping list, with a space between each:")
    arr = input()
    lst = list(map(str,arr.split( )))
    #print(lst)
    print()
    time.sleep(0.5)
    print("Is this all you need to buy today?")
    a = input()
    ans = a.lower()
    #print(ans)
    if ans =='yes':
        time.sleep(0.5)
        le = len(lst)
        print("You have {0} items on your list.".format(le))
        print()
        print("This is your shopping list for today:")
        print()
        for le in lst:
            print(le)
            time.sleep(0.5)

    elif ans =='no':
        time.sleep(0.5)
        print("Add additional items to your shopping list")
        arr2 = input()
        lst2 = list(map(str,arr2.split(' ')))
        lst.extend(lst2)
        print(lst)
        le = len(lst)
        print("You have {0} items on your list.".format(le))
        print()
        print("This is your shopping list for today:")
        for le in lst:
            print(le)
            time.sleep(0.5)
        
        
        

        
