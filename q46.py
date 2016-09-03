from sieve import sieve

primeList = set(sieve(10000000))
squareList = [x*x for x in range(1,4000)]

for i in xrange (9,10000000,2):
    if not(i in primeList):
        valid = False
        for j in squareList:
            if (i-2*j)<1:
                break
            elif ((i-2*j) in primeList):
                valid = True

        if not valid:
            print i
            break