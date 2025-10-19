from math import sqrt


def factors(n):
    result = []

    for i in range(1, int(sqrt(n))):
        if n % i == 0:
            result.append(i)
        if n // i != i:
            result.append(n // i)
    result.sort()
    return result


print(factors(36))
