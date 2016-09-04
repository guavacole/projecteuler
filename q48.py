sum = 0

for number in range (1,1001):
    tenDigits = 1
    for expo in range (0,number):
        tenDigits *= number
        if len(str(tenDigits))>10:
            tenDigits = int(''.join(list(str(tenDigits))[-10:]))

    sum += tenDigits

print int(''.join(list(str(sum))[-10:]))