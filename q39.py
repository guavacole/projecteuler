allPrimeSquares = []
for i in range(0,1000):
    allPrimeSquares.append(i*i)

setOfPrimes = set(allPrimeSquares)

max = 0
maxcount = 0
for i in range(3,1001):
    count = 0
    for first in range (2,i):
        for second in range (1,first):
            if(first + second)<i:
                if(allPrimeSquares[first]-allPrimeSquares[second])==allPrimeSquares[i-(first+second)]:
                    count += 1
    if count > maxcount:
        print i
        maxcount = count
        max = i

print max