def armstrong_number(n):
    num = n
    total = 0
    no_of_digits = len(str(n))

    while num > 0:
        last_digit = num % 10
        total = total + (last_digit**no_of_digits)
        num = num // 10

    #     # if total == n:
    #     #     return "It is an armstrong number."
    #     # else:
    #     #     return "Its not an armstrong number."

    #     if total == n:
    #         print("It is an armstrong number.")
    #     else:
    #         print("Its not an armstrong number.")

    # # print(armstrong_number(153))
    # # print(armstrong_number(221))

    # armstrong_number(153)
    # armstrong_number(221)

    return total == n


n = 153


if armstrong_number(n):
    print(f"{n} is an armstrong number.")
else:
    print(f"{n} is not an armstrong number.")
