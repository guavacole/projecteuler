from sieve import sieve,choose
from itertools import permutations

primeList = set(sieve(10000))
usedNumbers = [True]*10001

for number in range (1000,10000):
    if(usedNumbers[number]):
        permutation = filter(lambda x: x>999,map(lambda x:int(''.join(x)),list(set(list(permutations(list(str(number))))))))
        for numbers in permutation:
            usedNumbers[numbers] = False
        permutation= filter(lambda x:x in primeList, permutation)
        if len(permutation)>=3:
            choices =  list(choose(permutation,3))
            for choice in choices:
                dif1 = abs(choice[1]-choice[0])
                dif2 = abs(choice[2]-choice[1])
                dif3 = abs(choice[2]-choice[0])
                if dif1 == dif2 or dif1 == dif3 or dif2 == dif3:
                    print choice


