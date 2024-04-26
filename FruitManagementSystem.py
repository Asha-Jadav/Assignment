FruitManagement = {} # blank dictionary

def menu():
    
    menu = """
                    Fruit Market Manager

                    1) Add Fruit Stock
                    2) View Fruit Stock
                    3) Update Fruit Stock
    """ 
    print(menu)

def AddFruit():
    print("ADD FRUIT STOCK")
    name = input("Enter Fruit Name : ")
    qty = int(input("Enter Qty (in kg) : "))
    price = int(input("Enter Price : "))

    FruitStock = {} # Sub Dictionary

    #FruitManagement["name"] = name
    FruitStock["qty"] = qty
    FruitStock["price"] = price

    FruitManagement[name] = FruitStock
    #print(FruitStock)

def ViewFruitStock():
    print("---------------------------------")
    print(FruitManagement)

#def updateFruitStock()

role = """
                    WELCOME TO FRUIT MARKET

                    1) Manager
                    2) Customer
    """
print(role)
r1 = int(input("Enter Your Role  1 or 2 : "))
if r1 == 1:
    flag = True
    while flag:
        menu()
        choice = int(input("Enter your choice : "))
        if choice == 1:
            AddFruit()
        elif choice == 2:
            ViewFruitStock()
        #elif choice == 3:
            #updateFruitStock()
        else :
            print("invalid Input")
        cont = input("Do you want to perform more operations : press y for yes and n for no : ").lower()
        if cont == 'y':
            flag = True
        else:
            flag = False
elif r1 == 2:
    print("You Are Customer")
else:
    print("Invalid Input")

