def factorial(n):
    num =1
    for i in range(2,n+1):
        num = num*i
    return num

total = 0
for i in range (20,101):
    for j in range (1,i):
        if(factorial(i))/(factorial(j) *factorial(i-j)) > 999999:
            total = total + (i + 1) - 2 * (j)
            break
print total
