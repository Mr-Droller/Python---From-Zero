def reverse_string(string):
    if len(string) == 0:
        return ""
    else:
        return string[-1] + reverse_string(string[:-1])


def palindrome_checker(string):
    temp = reverse_string(string)
    if temp == string:
        return True
    else:
        return False


string = "racecar"
result = palindrome_checker(string)
print(result)

//begineer level recursion
