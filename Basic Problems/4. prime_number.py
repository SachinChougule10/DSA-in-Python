from math import *

num = int(input("Enter a number : "))

if num < 2:
    print("Number is not prime.")
else:
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            print("Number is not prime.")
            break
    else:  # The else block after a for only executes if the for loop finishes without hitting a break.
        print("Number is prime.")


# The else block after a for only executes if the for loop finishes without hitting a break.
#  The else block after a for is NOT like an if...else.
#  It's a special Python feature that only executes when the for finishes without a break.
