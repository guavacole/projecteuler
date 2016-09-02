from sieve import all_perms
pan = ['0','1','2','3','4','5','6','7','8','9']

def ruleCheck(intList):
    if int(''.join(intList[1:4])) % 2 ==0 and int(''.join(intList[2:5])) % 3 ==0 and int(''.join(intList[3:6])) % 5 ==0 and int(''.join(intList[4:7])) % 7 ==0 and int(''.join(intList[5:8])) % 11 ==0 and int(''.join(intList[6:9])) % 13 ==0 and int(''.join(intList[7:10])) % 17 ==0:
        return True
    return False


print sum(map(lambda x:int(''.join(x)),filter(ruleCheck,list(all_perms(pan)))))
