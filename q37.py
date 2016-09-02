from sieve import sieve

truncated = []
primes = set(sieve((10000000)))

for number in range (10,10000000):
    if len(truncated)==11:
        break

    numbers = list(str(number))
    valid = True
    for i in range (len(numbers)):
        if not valid:
            break
        if not int(''.join(numbers[i:])) in primes:
            valid = False

        if not int(''.join(numbers[0:i+1])) in primes:
            valid = False

    if valid:
        truncated.append(number)

total = 0

for i in range (11):
    total+=truncated[i]

print total
print truncated

