#script should return [1, 2, 4, 5, 6, 7, 8, 9]

list_of_arrays = [[3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]]

#convert each array to a set to remove duplicates within array
list_of_sets = [set(array) for array in list_of_arrays]

#initialize an empty set for a symmetric difference
sym_diff = set()

#compute symmetric difference iteratively 
for s in list_of_sets:
    sym_diff = sym_diff.symmetric_difference(s)

#convert result to a list
result = list(sym_diff)

print(result)
