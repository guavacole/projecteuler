from sieve import sieve

primeList = sieve(1000000)
primeSet = set(primeList)
length = len(primeList)
biggieSmalls = 0
tupac = 0

sumList = []
sums = 0
for number in primeList:
    sums += number
    sumList.append(sums)


for count,prime in enumerate(primeList):
    for index in range (count,length):
        sumList[index] = sumList[index] - prime
        if sumList[index] in primeSet and (index-count)>biggieSmalls:
            tupac = sumList[index]
            biggieSmalls = (index-count)
    print tupac
print tupac







