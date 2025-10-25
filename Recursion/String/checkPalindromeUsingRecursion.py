def check_palindrome(my_string, left, right):
    if left >= right:
        return True
    if my_string[left] != my_string[right]:
        return False

    return check_palindrome(my_string, left + 1, right - 1)


my_string = "ANBCDDCBNA"
print(check_palindrome(my_string, 0, len(my_string) - 1))
