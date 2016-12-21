f = open('poker.txt','r')

def isDefined(input):
    if input == -1:
        return False
    return True

def takeValue(hand):
    return map(lambda x: x[0],hand)

def takeSuit(hand):
    return map(lambda x: x[1],hand)

suits = ['D','S','H','C']
values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
hierarchy = {'2': 0,'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'T':8,'J':9,'Q':10,'K':11,'A':12}


def highCard(hand):
    highCard = '2'
    for card in takeValue(hand):
        if hierarchy[card] > hierarchy[highCard]:
            highCard = card
    return highCard

def detectPair(hand):
    highPair = -1
    hand = takeValue(hand)
    for value in values:
        if hand.count(value) == 2:
            highPair = value
    return highPair

def detect2Pair(hand):
    highPair = -1
    hand = takeValue(hand)
    for value in values:
        if hand.count(value) == 2:
            if isDefined(highPair):
                return value
            highPair = value
    return -1

def detectTriple(hand):
    hand = takeValue(hand)
    for value in values:
        if hand.count(value) == 3:
            return value
    return -1

def detectStraight(hand):
    hand = sorted(map(lambda x:hierarchy[x],takeValue(hand)))
    if hand == [12,0,1,2,3]:
        return '5'
    if hand[0] == hand[1] - 1 and hand[1] == hand[2] - 1 and hand[2] == hand[3] - 1 and hand[3] == hand[4] - 1 :
        return values[hand[4]]
    return -1

def detectFlush(hand):
    hands = takeSuit(hand)
    for suit in suits:
        if hands.count(suit) == 5:
            return highCard(hand)
    return -1

def detectFullhouse(hand):
    if(isDefined(detectPair(hand)) and isDefined(detectTriple(hand))):
        return detectTriple(hand)
    return -1

def detectStrightFlush(hand):
    if(isDefined(detectStraight(hand)) and isDefined(detectFlush(hand))):
        return highCard(hand)
    return -1
def detectQuad(hand):
    hand = takeValue(hand)
    for value in values:
        if hand.count(value) == 4:
            return value
    return -1
def detectRoyal(hand):
    if(isDefined(detectStrightFlush(hand))):
        if sorted(map(lambda x:hierarchy[x],takeValue(hand))) == [8,9,10,11,12]:
            return 'A'
    return -1

supercount = 0
disp = {1: highCard,2: detectPair,3:detect2Pair,4:detectTriple,5:detectStraight,6:detectFlush,7:detectFullhouse,8:detectQuad,9:detectStrightFlush,10:detectRoyal}
for line in f:

    p1 = line.split()[:5]
    p2 = line.split()[5:]
    p1hand = 1
    p1value = -1
    p2hand = 1
    p1value = -1
    for i in range(1,11):
        if isDefined(disp[i](p1)):
            p1hand = i
            p1value = disp[i](p1)
        if isDefined(disp[i](p2)):
            p2hand = i
            p2value = disp[i](p2)

    if(p1hand>p2hand):
        supercount += 1
    if(p1hand==p2hand) and (hierarchy[p1value]>hierarchy[p2value]):
        supercount +=1
print supercount