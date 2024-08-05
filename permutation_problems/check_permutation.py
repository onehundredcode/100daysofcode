#Given two strings, write a method to decide if one is a permutation of the other

def check_permutation(string_one, string_two):

    print("Comparing:" + "'" + string_one + "' " + "&" + " '" + string_two + "'")

    #check if strings are equal length
    if len(string_one) != len(string_two):
        print("Strings are not equal length.\nThey are not permutations of eachother.")
        return False
    
    #sort the strings in same order
    sorted_string_one = sorted(string_one)
    sorted_string_two = sorted(string_two)

    #check if the sorted strings are identical
    if sorted_string_one == sorted_string_two:
        print("Strings are permutations of each other.")
        return True
    else:
        print("Strings are not permutations of each eachother")
        return False          

#example usage
string_one = "god"
string_two = "cat"
print(check_permutation(string_one, string_two))

string_three = "dog"
print(check_permutation(string_one, string_three))