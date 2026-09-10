def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primes = []
for num in range(2, 21):
    if is_prime(num):
        primes.append(num)

print("All primes:", primes)

every_second = primes[0::2]
print("Every second prime:", every_second)