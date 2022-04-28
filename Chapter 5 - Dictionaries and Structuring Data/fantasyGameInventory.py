# inventory.py

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    total_items = 0
    for item, quantity in inventory.items():
        print(str(quantity)+' '+item)
        total_items += quantity
    print("Total number of items: "+str(total_items))


displayInventory(stuff)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0) #this adds a (defaulted to zero value) key to the inventory dict if it's not already there
        inventory[item] += 1 #and this increases that value by one, each time that item appears in the loot list
    return inventory

inv = {'gold coin': 42, 'rope': 1}
displayInventory(inv)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

inv = {'gold coin': 250, 'rope': 3, 'ruby': 5} #added in for my own benefit to practice
displayInventory(inv)
castleLoot = ['gold coin', 'rope', 'ruby']
inv = addToInventory(inv, castleLoot)
displayInventory(inv)