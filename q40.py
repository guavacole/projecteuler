biglist = []

for i in range (0,3000000):
    biglist.extend(list(str(i)))

print (int(biglist[1])*int(biglist[10])*int(biglist[100])*int(biglist[1000])*int(biglist[10000])*int(biglist[100000])*int(biglist[1000000]))
