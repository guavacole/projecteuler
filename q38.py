panSet = {'1','2','3','4','5','6','7','8','9'}
sets = [[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5],[1,2,3,4,5,6],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8,9]]
largestPan = 0
for number in range(1,100000):
    for setz in sets:
        total = []
        for i in setz:
            total.append(str(i*number))
        combined = ''.join(total)

        if(len(combined)==9) and set(combined)==panSet and int(combined)>largestPan:
            largestPan=int(combined)


print largestPan