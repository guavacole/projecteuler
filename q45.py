from sieve import genTriangle

pentaNum = {1}
for i in range (2,100000):
    pentaNum.add((i*(3*i-1)/2))

triangeNum = set(genTriangle(100000))

found = False
for i in range (2,100000):
    if (i*((2*i) -1) in triangeNum) and (i*((2*i) -1) in pentaNum):
        if not found:
            found = True
        elif found:
            print i*((2*i) -1)
            break
