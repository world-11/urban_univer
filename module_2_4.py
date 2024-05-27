numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1, len(numbers)):
    is_prime = True
    for x in range(2, numbers[i]):
        if numbers[i] % x == 0:
            is_prime = False
            break
    if is_prime == False:
        not_primes.append(numbers[i])
    else:
        primes.append(numbers[i])
print('Primes:', primes)
print('Not Primes:', not_primes)

