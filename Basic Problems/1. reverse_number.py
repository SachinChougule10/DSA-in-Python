number=5873

n = number

while n>0:
    last_digit = n % 10
    n = n // 10
    print(last_digit,end=' ')