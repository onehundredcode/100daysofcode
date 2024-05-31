#create a new dictionary from 2d array

#Efficient and concise way to create dictionaries - {key : value for element in iterable}

current_inventory = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
]

def array_to_dictionary(array):

    #{key : value for element in iterable}
    inventory_dict = {
        item[0] : item [1] #assiging keys and values to dictionary using indices of array
        for item in current_inventory #iterating through array
    }

    print(inventory_dict.items())

array_to_dictionary(current_inventory)