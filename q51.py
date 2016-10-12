from sieve import sieve

stringlist = ['0','1','2','3','4','5','6','7','8','9']
primeList = sieve(10000000)
primeSet = set(primeList)
usedPrimes = set()
for prime in primeList:
    if not prime in usedPrimes:
        listform = list(str(prime))
        for number in stringlist:
            if(number in listform):
                count = 0
                cloned = listform[:]
                indexs = []
                for i in range(0,len(listform)):
                    if listform[i] == number:
                        indexs.append(i)

                for replacement in stringlist:
                    for values in indexs:
                        cloned[values] = replacement
                    num = int(''.join(cloned))
                    if(num in primeSet and not(0 in indexs and replacement == '0')):
                        count = count +1
                    usedPrimes.add(num)
                if(count == 8):
                    print number
                    print listform
                    exit()






