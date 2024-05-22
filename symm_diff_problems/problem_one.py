#function takes 2 or more arrays

#returns array of symetric difference 

#returned array should have unique values ONLY

def sym_diff(*arrays):
    #Convert arrays to sets
    set1 = set(arr1)
    set2 = set(arr2)

    #Compute symmetric difference
    result = set1.symmetric_difference(set2)

    #Convert result to list
    return list(result)



arr1 = [1,2,3]
arr2 = [5,2,1,4]

answer = sym_diff(arr1, arr2)

print(answer)