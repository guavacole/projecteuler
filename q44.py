pentaNums = {1}
pentaList = [1]
for i in range (2,5000):
    pentaNums.add((i*(3*i-1)/2))
    pentaList.append(i*(3*i-1)/2)

minval = 99999999
for i in range (1,3000):
    for j in range (0,i):
        if (pentaList[i]-pentaList[j] in pentaNums) and (pentaList[i]+pentaList[j] in pentaNums) and (pentaList[i]-pentaList[j]<minval):
            minval = pentaList[i]-pentaList[j]
print minval