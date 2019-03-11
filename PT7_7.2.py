import time

def l():
    highway = 110
    road = 70
    town = 50
    spaceship = 200
    print("This program calculates your travel time")
    print("How many KM/s are you traveling today?")
    dst = float(input())
    print()
    print("What type of road are you driving on today?")
    print()
    time.sleep(0.5)
    print("H = Highway")
    time.sleep(0.5)
    print("R = Road")
    time.sleep(0.5)
    print("T = Town")
    time.sleep(0.5)
    print("S = Spaceship")
    print()
    tpe = input()
    if tpe =='H':
        time.sleep(0.5)
        tme = dst/highway
        print()
        print("It will take an estimated {0} hours to reach your destination {1} KM/s away at a speed of {2}KM/h.".format(round(tme, 2), dst, highway))
    elif tpe =='R':
        tme = dst/road
        print()
        print("It will take an estimated {0} hours to reach your destination {1} KM/s away at a speed of {2}KM/h.".format(round(tme, 2), dst, road))
    elif tpe =='T':
        tme = dst/road
        print()
        print("It will take an estimated {0} hours to reach your destination {1} KM/s away at a speed of {2}KM/h.".format(round(tme, 2), dst, town))
    elif tpe =='S':
        tme = dst/spaceship
        print()
        print("It will take an estimated {0} hours to reach your destination {1} KM/s away at a speed of {2}KM/h.".format(round(tme, 2), dst, spaceship))
    else:
        print()
        print("You didn't select a type of road, Idiot!")
