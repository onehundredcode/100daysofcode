#Compare current inventory stored in a 2D array with new inventory stored in another 2D array

#Update the current inventory array with the new inventory

#Output the current inventory array with the new inventory in alphabetical order

current_inventory = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
]

new_inventory = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
]

def update_inventory(*arrays):
    #convert current inventory to dictionary
    inventory_dict = {item[1]: item[0] for item in current_inventory} 

    #update the dictionary with new inventory items
    for quantity, item in new_inventory:
        if item in inventory_dict:
            inventory_dict[item] += quantity
        else:
            inventory_dict[item] = quantity
            

    #convert dictionary back to a list of lists
    updated_inventory = [[quantity, item] for item, quantity in inventory_dict.items()]

    #sort the updated inventory alphabetically by item name
    updated_inventory.sort(key=lambda x: x[1])

    #print updated inventory
    for item in updated_inventory:
        print(item)
    

update_inventory(current_inventory, new_inventory)


