def exponentiation(number, base):
    if base == 0:
        return 1
    else:
        return number * exponentiation(number, base - 1)


result = exponentiation(2, 1)
print(result)

// begineer level recursion
