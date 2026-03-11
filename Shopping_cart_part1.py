import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="maggi@522",
    database="grocery_store"
)

cursor = conn.cursor()
Items = {}

cursor.execute("SELECT * FROM items")
rows = cursor.fetchall()

for row in rows:
    Items[row[0]] = {
        "Itemname": row[1],
        "costperItem": row[2],
        "Quantity": row[3]
    }

print(Items.items())

print(f"{'Sr.no':<10} {'Itemname':<15} {'costperItem':>10} {'Quantity':>15}")
print("-" * 55)

# 2. Print the Data Rows
for sn, details in Items.items():
    name = details["Itemname"]
    cost = details["costperItem"]
    qty = details["Quantity"]    
    print(f"{sn:<10} {name:<15} {cost:>10} {qty:>15}")

isValidInput = False
cart = {}
totalPrice = 0

while  not isValidInput:
    print("What do you want to purchase?")
    purchaseNum = int(input())
    if purchaseNum>0 and len(Items) >=purchaseNum:
        purchaseItem = Items[purchaseNum]["Itemname"]
        availableQuantity = Items[purchaseNum]["Quantity"]
        priceEachItem = Items[purchaseNum]["costperItem"] 
        print(f"How many {purchaseItem} you wanto buy?")
        requiredQuantity = int(input())
        if requiredQuantity>availableQuantity:
            print(f"Available quantity of {purchaseItem} is {availableQuantity}")
            print("Do you want to continue shopping? Y/N")
            userOption = input().upper()
            if userOption == "N":
              isValidInput = True
              break

        else:
            cart[purchaseNum] = {
                "Itemname": purchaseItem,
                "Quantity": requiredQuantity,
                "Price": priceEachItem * requiredQuantity
            }
            print("Items added in the cart. Do you want to continue shopping? Y/N")
            userOption = input().upper()
            if userOption == "N":
                isValidInput = True
                break
    else:
        print("Invalid")
        print("Do you want to continue shopping? Y/N")
        userOption = input().upper()
        if userOption == "N":
            isValidInput = True
            break

if len(cart)>0:
        print("Enter your Name:")
        customerName = input()
        print("Enter your Address:")
        customerAddress = input()
        print("Enter your distance from the store:")
        customerHomeDist = int(input())
        print(f"{'Sr.no':<10} {'Item':<15} {'Quantity':>10} {'Price':>15}")
        print("-" * 55)

        # 2. Print the Data Rows
        for sn, details in cart.items():
            name = details["Itemname"]
            qty = details["Quantity"]
            cost = details["Price"]
            totalPrice = totalPrice + cost    
            print(f"{sn:<10} {name:<15} {qty:>10} {cost:>15}")
            Items[sn]["Quantity"]=Items[sn]["Quantity"]-qty

deliverycharges=0
if customerHomeDist <=15:
    deliverycharges=50
    print("delivery charge is 50")
elif customerHomeDist <=30:
    deliverycharges=100
    print("delivery charge is 100")
else:
    print("Delivery not available")
    
print(f"Total Products cost:{totalPrice}")
print(f"Total BillAmount including delivery charges:{totalPrice+deliverycharges}")
print(f"customer name:{customerName}")
print(f"customer Address:{customerAddress}")
print("Have A NICE DAY,PLEASE VISIT AGAIN")
print("**********Remaining items in store************************")
print(f"{'Sr.no':<10} {'Item':<15} {'Quantity':>10} {'Cost/Item':>15}")
print("-" * 55)

# 2. Print the Data Rows
for sn, details in Items.items():
    name = details["Itemname"]
    qty = details["Quantity"]
    cost = details["costperItem"]    
    sql = "UPDATE items SET quantity = %s WHERE itemname = %s"
    val = (qty, name)
    cursor.execute(sql, val)
    print(f"{sn:<10} {name:<15} {qty:>10} {cost:>15}")
cursor.execute(
    "INSERT INTO orders (customer_name,address,distance,total_amount) VALUES (%s,%s,%s,%s)",
    (customerName, customerAddress, customerHomeDist, totalPrice+deliverycharges)
)

conn.commit()
cursor.close()
conn.close()





            


