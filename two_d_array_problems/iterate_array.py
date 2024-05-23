#Iterate through a 2D array and print the values as two sepearate arrays

#One array should have the numbers

#The other array should have the names

current_inventory = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
]

def iterate_array(array):
    #initializing empty list to store values  of numbers and names
    inventory_number = []
    inventory_names = []

    #loop to iterate through each row
    for row in array:
        #assiging number and names to variables
        number = row[0]
        name = row[1]
        #appending numbers and names to empty list
        inventory_number.append(number)
        inventory_names.append(name)
    print("These are the item numbers: " , inventory_number)
    print("These are items names: ", inventory_names)
        

iterate_array(current_inventory)