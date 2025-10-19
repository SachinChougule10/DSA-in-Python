# is_prime = [True] * 10
# print(is_prime)

# is_prime[0] = is_prime[1] = False

# print(is_prime)

# print(sum(is_prime))

# print(sum(i for i, prime in enumerate(is_prime) if prime))

squares = (i * i for i in range(5))

print(next(squares))
print(next(squares))
