def factors(n):
    result = []

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            result.append(i)
    result.append(n)

    # return result

    print(result)


# print(factors(20))

factors(20)
