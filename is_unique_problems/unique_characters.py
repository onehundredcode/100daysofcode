#implement an algorithm to determine if a string has all unique characters


def unique_characters(string):

    #Sort the string in lexicographical order
    sorted_string = sorted(string)

    #check for adjacent duplicates
    #subtracting 1 from length of sorted string to make sure loop stops on second to last character
    for i in range(len(sorted_string) - 1):

        #if statement to validate if their is a duplicate character
        if sorted_string[i] == sorted_string[i + 1]:
            return False
    return True

# Example usage
string = "abcdef"
print(unique_characters(string))  # Output: True

string = "abcdea"
print(unique_characters(string))  # Output: False
    