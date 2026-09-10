inventory = {}

while True:
    choice = input("1.Add Stock\n2.Remove Stock\n3.View Inventory\n4.Exit\n")

    if choice == "4":
        print("Exiting.....")
        break

    elif choice == "1":
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity to add: "))

        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity

        print(f"{quantity} {item} added. Current stock: {inventory[item]}")

    elif choice == "2":

        item = input("Enter item name: ")
        quantity = int(input("Enter quantity to remove: "))

        if item not in inventory:
            print(f"{item} does not exist in inventory")

        elif inventory[item] - quantity < 0:
            print(f"Cannot remove {quantity} — only {inventory[item]} in stock")

        else:
            inventory[item] -= quantity
            print(f"{quantity} {item} removed. Current stock: {inventory[item]}")

    elif choice == "3":

        if inventory:
            print(inventory)
            
        else:
            print("Inventory is empty")

    else:
        print("Please enter a valid choice")