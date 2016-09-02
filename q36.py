sum = 0
for i in range(1000000):
    binary=list(bin(i))
    if (list(str(i)) == list(str(i))[::-1]) and (binary[2:] == binary[len(binary)-1:1:-1]):
        sum += i

print sum