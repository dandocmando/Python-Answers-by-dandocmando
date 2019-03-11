import time

def l():
   print("This Program will change a hexadeciamal into decimal.")
   time.sleep(1)
   print("Please choose a hexadecimal:")
   dummy = input()
   time.sleep(1)
   hx = int(dummy, 16)
   print()
   print((hx), "in decimal")
