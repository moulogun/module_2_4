numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_prime = []
is_prime = False
d = 0
for i in numbers:
    for g in range(2, (i + 1)):
        if (i % g) == 0:
            d = d + 1
        else:
            continue
    if d == 1:
        is_prime = True
    elif d > 1:
        is_prime = False
    else:
        continue
    if is_prime == True:
        primes.append(i)
    else:
        not_prime.append(i)
    d = 0
print('Primes:', primes)
print('Not Primes:', not_prime)
