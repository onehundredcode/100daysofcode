#function should return [3,4,5]


arr1 = [1, 2, 3, 3]
arr2 = [5, 2, 1, 4]


def problem_three(*arrays):
    set1 = set(arr1)
    set2 = set(arr2)

    sym_diff = set1.symmetric_difference(set2)

    return list(sym_diff)


answer = problem_three(arr1, arr2)
print(answer)