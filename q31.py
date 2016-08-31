coins = [1, 2, 5, 10, 20, 50, 100]
matrix = [[0 for x in range(7)]for y in range(201)]
matrix[0] = [1,1,1,1,1,1,1]

for y in range (1,201):
    for x in range (7):
        if(x>0):
            matrix [y][x] += matrix[y][x-1]
        if((y-coins[x])>=0):
            matrix [y][x] += matrix[y-coins[x]][x]

print matrix[200]+1