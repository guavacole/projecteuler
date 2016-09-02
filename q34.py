factorials = [1,1,2,6,24,120,720,5040,40320,362880]
total =0
for number in range (3,10000000):
    if number == sum(map(lambda x:factorials[int(x)],list(str(number)))):
        total +=number



print total