def check_palindrome(n):

    number = n

    result = 0

    while number > 0:
        last_digit = number % 10
        result = (result * 10) + last_digit
        number = number // 10

    if result == n:
        return "Number is palindrome."
    else:
        return "Number is not palindrome."


print(check_palindrome(1221))
print(check_palindrome(5222))
