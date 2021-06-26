import cart as crt
import welcome as wc
import data

def showRoom():
    print("\n============== Showroom ==============")
    print("\n1.Show items")
    print("2.Add to cart")
    print("3.Go to cart")
    print("4.Exit")
    n = int(input("\n>>> "))

    if(n == 1):
        printItems()
        showRoom()
    elif(n == 2):
        itemCode = int(input("\nEnter item code >>> "))
        qty = int(input("Enter quantity >>> "))

        item = getItemRemainQtyByItemCode(itemCode)

        if(not item):
            print("\nItem entered not found")
            showRoom()

        if(item['In Stock'] < qty):
            print("\nSorry, there are only ", item['In Stock'], " items in stock\n")
            showRoom()
        else:
            addToCart(item, qty)
            print("\nItem added to the cart successfully")
            showRoom()
    elif(n == 3):
        crt.cart()
    elif(n == 4):
        wc.welcome();
    else:
        print("\nInvalid Input, Please enter a valid number")
        showRoom()

def getItemRemainQtyByItemCode(itemCode):
    for i in data.inventory:
        if(i['Item Code'] == itemCode):
            return i

    return False

def printItems():
    print("\n------------ Showcase ------------")
    for item in data.inventory:
        for key in item.keys():
            print(key, ": ", item[key])
        print("-------------------------------\n")

def addToCart(item, qty):
    cartItem = {}
    cartItem['Item Code'] = item['Item Code']
    cartItem['Item Name'] = item['Item Name']
    cartItem['Qty'] = qty
    cartItem['Item Price'] = item['Price']
    cartItem['Item Total'] = item['Price'] * qty
    data.shoppingCart.append(cartItem)

    for i in data.inventory:
        if(i['Item Code'] == item['Item Code']):
            i['In Stock'] -= qty
