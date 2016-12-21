def sumDigits(num):
    return sum(map(lambda x: int(x),str(num)))

max = 0
for i in range (1,100):
    current = i

    for ex in range (1,100):

        if sumDigits(current)>max:
            max = sumDigits(current)
        current = current * i

print max