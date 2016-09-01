
total = 0
setOfAll = {0}
allNumber = [0,1,2,3,4,5,6,7,8,9]
for x in range(10):
    for y in range(1000,10000):
        setOfNums = set(list(str(x))).union(set(list(str(y))))
        if len(list(setOfNums))==5:
            setOfNums=setOfNums.union(set(str(x*y)))
            if(len(list(setOfNums))==9) and  (not(setOfNums.__contains__('0')) and len(str(x*y))==4):
                print x, " ", y
                setOfAll.add(x*y)


for x in range(10,100):
    for y in range(100,1000):
        setOfNums = set(list(str(x))).union(set(list(str(y))))
        if len(list(setOfNums))==5:
            setOfNums=setOfNums.union(set(str(x*y)))
            if(len(list(setOfNums))==9) and (not (setOfNums.__contains__('0')) and len(str(x*y))==4):
                print x, " ",y
                setOfAll.add(x*y)

for i in list(setOfAll):
    total+=i

print total