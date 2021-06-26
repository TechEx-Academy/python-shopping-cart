import showroom as sr
import checkout as chk
import welcome as wc
import data

def cart():
    print("\n============== Cart ==============")
    print("\n1.Show cart")
    print("2.Checkout")
    print("3.Remove from cart")
    print("4.Continue shopping")
    print("5.Exit\n")
    n = int(input(">>> "))

    if(n == 1):
        printCartItems()
        cart()
    if(n == 2):
        chk.checkout(getTotal())
    elif(n == 3):
        itemCode = int(input("\nEnter item code >>> "))
        qty = int(input("Enter removing qty >>> "))
        removeItem(itemCode, qty)
        cart()
    elif(n == 4):
        sr.showRoom()
    elif(n == 5):
        wc.welcome()
    else:
        print("\nInvalid input, please enter a valid number")
        cart()


def printCartItems():
    print("\n-------------- Cart --------------")
    for item in data.shoppingCart:
        for key in item.keys():
            print(key, ": ", item[key])
        print("---------------------------------\n")

    total = getTotal()

    print("===============================")
    print("Total: ", total)
    print("===============================\n")


def getTotal():
    total = 0
    for item in data.shoppingCart:
        total += item['Item Price']*item['Qty']
    return total

def removeItem(itemCode, qty):
    found = False
    for item in data.shoppingCart:
        if(item['Item Code'] == itemCode):
            found = True
            if(item['Qty'] < qty):
                print("\nYou only have ", item['Qty'], " items in the cart")
                return
            else:
                item['Qty'] -= qty
    if not found:
        print("\nItem code ", itemCode, " not in the cart")
        return
    return
