def main():
    print("What message do you want to loop?")
    i = (input())
    print("How many times?")
    dummy = int(input())
    print(i)
    for counter in range(dummy):
        print(i)

