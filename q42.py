from sieve import genTriangle
file = open("q42words.txt", 'r')

wordList = file.read().split('","' )
wordList[0] = 'A'
wordList[len(wordList)-1] = 'YOUTH'

triangleList = set(genTriangle(40))
count = 0
for words in wordList:
    if triangleList.__contains__(sum(map(lambda x: ord(x)-64,list(words)))):
        count += 1

print count