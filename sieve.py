def sieve(number):
    prime = [True]*(number+1)
    listOfPrime = []
    for i in range(2,number+1):
        if prime[i]:
            listOfPrime.append(i)
            count = i*2
            while count<number+1:
                prime[count] = False
                count += i

    return listOfPrime



list = sieve(1000000)

