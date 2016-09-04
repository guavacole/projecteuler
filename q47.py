from sieve import sieve

primeList = sieve(10000000)


def primefactor(number):
    count = 0
    occurence = 0
    listOfFactors = []

    while number>1 or not occurence==0:
        if number%primeList[count]==0:
            occurence+=1
            number = number/primeList[count]
        else:
            if not occurence == 0:
                listOfFactors.append((primeList[count],occurence))
                occurence=0
            count+=1
        if len(listOfFactors)==5:
            break

    if len(listOfFactors) ==4:
        return listOfFactors
    else:
        return False



listOfFactors = [0]
listOfFactors.append(primefactor(1))
listOfFactors.append(primefactor(2))
listOfFactors.append(primefactor(3))
listOfFactors.append(primefactor(4))


for i in range (5,10000000):
    listOfFactors.append(primefactor(i))
    if not(primefactor(i)==False or primefactor(i-1)==False or primefactor(i-2)==False or primefactor(i-3)==False):
        pool = {0}
        valid = True
        for number in range (0,4):
            if not valid:
                break
            for factors in listOfFactors[i-number]:
                if(factors in pool):
                    valid = False
                    break
                pool.add(factors)


        if valid:
            print i
            break





