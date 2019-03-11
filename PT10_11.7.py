import time

def l():
   print("This Program will change a decimal into binary.")
   time.sleep(1)
   print("Please choose a decimal:")
   dummy = input()
   time.sleep(1)
   hx = int(dummy, 16)
   print()
   print((hx), "in decimal")
