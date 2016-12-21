def isPalindrome(num):
    return (str(num) == str(num)[::-1])

total = 10000
for num in range(0,10000):
    current = num
    for i in range(0,50):
        current += int(str(current)[::-1])
        if isPalindrome(current):
            total -= 1
            break
print total



