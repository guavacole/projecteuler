class frac:
    numerator = 0
    denominator = 0

    def __init__(self,num,den):
        self.numerator = num
        self.denominator = den

    def inverse(self):
        temp = self.denominator
        self.denominator = self.numerator
        self.numerator = temp
        return self

    def add(self,num):
        self.numerator = self.numerator + num * self.denominator
        return self

    def check(self):
        return len(str(self.numerator + self.denominator)) > len(str(self.denominator))

    def show(self):
        print self.numerator , "/" , self.denominator

    def toDecimal(self):
        print float(self.numerator) / self.denominator

first = frac(1,2)

count = 0
for i in range (0,999):
    first = first.add(2)
    first = first.inverse()
    if first.check():
        count += 1

print count




