#find overlapping values for 2,3 and (5,6,7,10) of which each have same number of overlapping numbers
totalOverlap =0
two = [True]*601
for i in range (1,7):
    for exp in range (2,101):
        if(two[i*exp]):
            two[i*exp] = False
        else:
            totalOverlap+=1

three = [True]*401
for i in range (1,5):
    for exp in range (2,101):
        if(three[i*exp]):
            three[i*exp] = False
        else:
            totalOverlap+=1
other = [True]*201
for i in range (1,3):
    for exp in range (2,101):
        if(other[i*exp]):
            other[i*exp] = False
        else:
            totalOverlap+=4

print 99*99 - totalOverlap