#returned list should contain 3 unique elements

def problem_two(*arrays):
    set1 = set(arr1)
    set2 = set(arr2)

    sym_diff = set1.symmetric_difference(set2)

    return list(sym_diff)




arr1 = [1, 2, 3]
arr2 = [5, 2, 1, 4]

answer = problem_two(arr1, arr2)

print(answer)