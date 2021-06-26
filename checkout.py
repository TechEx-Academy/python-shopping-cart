import showroom as sr
import cart as crt

def checkout(total):
    print("\n============== Checkout ==============")
    print("Your bill is ", total, "\n")
    price = int(input("Enter money >>> "))

    pay = payment(total, price)
    if(pay):
        sr.showRoom()
    else:
        crt.cart()

def payment(total, money):
    if(money > total):
        balance = money - total
        print("\nThank you for shoppping with us! Your balance is ", balance)
        return True
    else:
        print("\nInsufficient amout")
        return False
