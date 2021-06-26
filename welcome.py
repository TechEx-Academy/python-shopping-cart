import showroom as sr

def welcome():
    print("\n============== Welcome to the TechEx Gadget Shop ==============")
    print("\n1.Got to show room")
    print("2.Exit")
    n = int(input("\n>>> "))

    if(n == 1):
        sr.showRoom();
    else:
        exit(0)
