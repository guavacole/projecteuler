#upper bound is 9^5 *6

total=0


for i in range (0,354294):
    if i == sum(map((lambda x: pow(int(x),5)), str(i))):
        total = total +i

print total-1

