total = 1
sidelength = 3
while sidelength<1002:
    square = sidelength*sidelength
    total += square*4 - (sidelength-1)*6
    sidelength+=2

print total
