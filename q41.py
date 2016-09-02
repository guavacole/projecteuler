from sieve import sieve,all_perms
setOfPrime = set(sieve(10000000))
lists = ['1','2','3','4','5','6','7']
#checkout dis sick one liner
print max(filter(setOfPrime.__contains__,map(lambda x:int(''.join(x)),all_perms(lists))))
