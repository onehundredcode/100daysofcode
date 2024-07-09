#using the "sorted" function will sort your data in lexicographical order

#Lexicographical order means it will sort your data type in ascending order

#Sorting strings
def sorting_strings(string):
    sorted_string = sorted(string)

    print(sorted_string)


my_string = "nbfjvhgtueszaowdfjcwsllsx"
sorting_strings(my_string) #prints a string in ascending order with duplicates placed next to eachother


#Sorting sets
def sorting_set(my_set):
    sorted_set = sorted(my_set)

    print(my_set)

my_set = {1,3,4,2,5,3,2,1,5,6,7,8,9,6,4,4}
sorting_set(my_set) #prints a list in ascending order, duplicates are removed by default because it is a set

#Sorting array
def sorting_array(array):
    sorted_array = sorted(array)

    print(sorted_array)

my_array = [1,4,3,5,67,5,4,3,2,4,5,6,8,9,8,7,5,43,23,2]
sorting_array(my_array) #print an array in ascending order with duplicates placed next to eachother 