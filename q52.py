def compare2(list1,list2):
    chart = [0,0,0,0,0,0,0,0,0,0]
    for i in list1:
        chart[i] = chart[i] + 1
    for i in list2:
        chart[i] = chart[i] - 1
    if chart == [0,0,0,0,0,0,0,0,0,0]:
        return True
    return False

for i in range(10,10000000):
    base = map(int,list(str(i)))
    for mult in range(2,7):
        if not compare2(base,map(int,list(str(i*mult)))):
            break
        if mult == 6:
            print i
            exit()


