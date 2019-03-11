import time

def l():
   print("This Program will change a decimal into hexadecimal.")
   time.sleep(1)
   print("Please choose a decimal:")
   dummy = int(input())
   time.sleep(1)
   print()
   time.sleep(0.5)
   print(hex(dummy), "in hexadecimal")
