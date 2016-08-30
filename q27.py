from sieve import sieve
primeList = set(sieve(5000000))
print "done"
maximum = 0
aa=0
bb=0
for a in range (-1000,1001):

    for b in range (-1000,1001):
        if(abs(b)in primeList):
           n=1
           while (True):
               if not((n*n + n*a +b) in primeList):
                    if (n-1)>maximum:
                        maximum = n-1
                        aa=a
                        bb=b
                    break
               else:
                    n+=1
print aa*bb
print aa
print bb