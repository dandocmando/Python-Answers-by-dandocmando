import time

def main():
    time.sleep(1)
    print("Enter Either 0 or 1")
    response = input()
    if response == "0":
        print("The light is off")
    elif response =="1":
        print("The light is on")

    else:
        print("Please enter 0 or 1")
        
