#Python Dictionary - a data structure that allows you to store and manage data in key value pairs. A dictionary allows you to look up a key and find its associated value

#Key (word) has a value (definition)

#Key's must be unique. Values can be duplicated

#Dictionaries have no specific order. Key and value pairs can be modified (mutable). Accessing values is quick and efficient.



#creating a dictionary
car = {
    "color": "Blue",
    "year": "2020",
    "make": "Honda",
    "model": "Civic",
    "mileage": 62000
}

#accessing values
print("The car details stored in my dictionary are: \n")
print(car.keys())
print(car.values())
print("\n")

#adding a new key-value pair
car["trim"] = "Sport"

#modifying existing value
car["color"] = "Grey"
print("Updating the car color of " + car["make"] + " " + car["model"] + " " + car["year"] + " to " + car["color"] )
print("New color of " + car["make"] + " " + car["model"] + " " + car["year"] + " is " + car["color"])

#deleting key-value pairs
del car["mileage"]
print("Deleting 'Mileage' key in car dictionary")
print(car.items())