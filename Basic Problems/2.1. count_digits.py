# We can count the number of digits using log10 and adding 1 to it and then converting it to integer.


from math import *


def count_digits(number):

    if number == 0:
        return "Undefined (log is only for positive numbers)"
    return int(log10(abs(number)) + 1)


print(count_digits(0))
print(count_digits(-2526))
print(count_digits(5569))


# The abs() function in Python returns the absolute value of a number.
# abs(num) ensures that num is always positive before applying log10().

# print(abs(10))    # Output: 10
# print(abs(-10))   # Output: 10
# print(abs(0))     # Output: 0
# print(abs(3 + 4j))  # Output: 5.0 (because sqrt(3² + 4²) = 5)


# 1. number = 0 → log10(0) is undefined (causes an error).
# 2. number < 0 → log10() is not defined for negative numbers.
