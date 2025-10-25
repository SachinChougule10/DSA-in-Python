def check_palindrome(my_string):
    left = 0
    right = len(my_string) - 1

    while left < right:
        if my_string[left] != my_string[right]:
            return False

        left += 1
        right -= 1

    return True


my_string = "ANBCDDCBNA"
print(check_palindrome(my_string))
