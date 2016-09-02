from sieve import sieve
primes = sieve(100)

def reduc(top,bot):
    for prime in primes:
        while (True):
            if(top%prime==0 and bot%prime==0):
                top = top/prime
                bot = bot/prime
            else:
                break
    return [top,bot]


results = []

for i in range (10,100):
    digits =  map(int,str(i))
    for j in range (i+1,100):
        digits2 = map(int,str(j))
        if(not(digits[1]==0 or digits2[1]==0)):
            if(digits[0]==digits2[0] and (reduc(i,j) == reduc(digits[1],digits2[1]))):
                results.append([i,j])
            elif (digits[0] == digits2[1] and (reduc(i, j) == reduc(digits[1], digits2[0]))):
                results.append([i, j])
            elif (digits[1] == digits2[0] and (reduc(i, j) == reduc(digits[0], digits2[1]))):
                results.append([i, j])
            elif (digits[1] == digits2[1] and (reduc(i, j) == reduc(digits[0], digits2[0]))):
                results.append([i, j])
numer = 1
denom = 1
for i in results:
    print i
    numer = numer*i[0]
    denom = denom*i[1]

print reduc(numer,denom)

