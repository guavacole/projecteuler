from sieve import sieve
count =0
primes = set(sieve(1000000))
for number in range (2,1000000):
    num = list(str(number))
    valid = True
    leng = len(num)
    if not(number in primes):
        valid = False

    for i in range(1,leng):
        if not valid:
            break
        num = num[1:leng]+[num[0]]
        if not int(''.join(num)) in primes:
            valid = False

    if valid:
        count += 1

print count