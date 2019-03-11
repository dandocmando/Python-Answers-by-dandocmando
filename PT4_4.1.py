import time

def l():
    #ask how old they are
    time.sleep(1)
    age = int(input("Enter your age: "))
    retirement = 65
    sum = 65-age
    if age >= 18:
     #tell them if they can vote
     time.sleep(1)
     print()
     print("You can Vote!")
     print()
    else:
      time.sleep(1)
      print()
      print("You can't Vote!")
      print()
       #tell them how long until they retire
    if age >=65:
          time.sleep(1)
          print()
          print("Your retired!")
          print()
    else:
        time.sleep(1)
        print()
        print("{0} years until you can retire".format(sum))
        print()
  
