from poker import *

def flushtest():
    counter = 0
    if flush(['2C', '3C', '5C', '8C', 'TC']) == True:
        counter = counter + 1
    if flush(['AS', '2S', '3S', 'KS', 'TS']) == True:
        counter = counter + 1
    if flush(['TD', 'KD', 'QD', 'JD', '2D']) == True:
        counter = counter + 1
    if flush(['TD', 'AD', 'QD', '2D', '5D']) == True:
        counter = counter + 1
    if flush(['2H', '5H', '4H', 'AH', '8H']) == True:
        counter = counter + 1
    if flush(['2C', '3S', '5C', '8C', 'TC']) == False:
        counter = counter + 1
    if flush(['AS', '2D', '3S', 'KD', 'TS']) == False:
        counter = counter + 1
    if flush(['TH', 'KH', 'QD', 'JH', '2D']) == False:
        counter = counter + 1
    if flush(['4H', '4C', '4S', '4D', '5S']) == False:
        counter = counter + 1
    if flush(['2H', '5H', '4H', 'AD', 'AC']) == False:
        counter = counter + 1
    return counter

def straighttest():
    counter = 0
    if straight(['2C', '3D', '4S', '5D', '6H']) == True:
        counter = counter + 1
    if straight(['AC', '2H', '3C', '4D', '5C']) == True:
        counter = counter + 1
    if straight(['AD', 'KH', 'QC', 'JC', 'TC']) == True:
        counter = counter + 1
    if straight(['8D', 'TH', 'QC', '9C', 'JC']) == True:
        counter = counter + 1
    if straight(['8D', '6D', '4D', '5D', '7H']) == True:
        counter = counter + 1
    if straight(['8D', '9H', 'JH', 'JC', 'QC']) == False:
        counter = counter + 1
    if straight(['8D', '8H', '8C', '8S', 'QC']) == False:
        counter = counter + 1
    if straight(['AS', '2S', '3S', 'KS', 'TS']) == False:
        counter = counter + 1
    if straight(['AS', '2S', 'AH', '5S', '4S']) == False:
        counter = counter + 1
    if straight(['QS', 'KS', 'AS', '2H', '3H']) == False:
        counter = counter + 1
    return counter

def ranktest():
    counter = 0
    if rank(['QS', 'KS', 'AS', '2H', '3H']) == 0:
        counter = counter + 1
    else:
        print "Failed high card"
    if rank(['QS', 'QH', 'AS', '2H', '5D']) == 1:
        counter = counter + 1
    else:
        print "Failed pair"
    if rank(['QS', 'QH', '8S', '8D', '3D']) == 2:
        counter = counter + 1
    else:
        print "Failed two pair"
    if rank(['QS', 'QH', 'QD', '8D', 'TH']) == 3:
        counter = counter + 1
    else:
        print "Failed triple"
    if rank(['AD', 'KH', 'QC', 'JC', 'TC']) == 4:
        counter = counter + 1
    else:
        print "Failed straight"
    if rank(['TD', 'AD', 'QD', '2D', '5D']) == 5:
        counter = counter + 1
    else:
        print "Failed flush"
    if rank(['QS', 'QH', '8S', '8D', '8C']) == 6:
        counter = counter + 1
    else:
        print "Failed full house"
    if rank(['4H', '4C', '4S', '4D', '5S']) == 7:
        counter = counter + 1
    else:
        print "Failed four of a kind"
    if rank(['7D', 'TD', '8D', 'JD', '9D']) == 8:
        counter = counter + 1
    else:
        print "Failed straight flush"
    if rank(['AD', 'KD', 'QD', 'TD', 'JD']) == 8:
        counter = counter + 1
    else:
        print "Failed royal flush"
    return counter

def winnertest():
    answer = [2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 1, 1, 1, 2, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1]
    parse = open("hands.txt", 'r')
    counter = 0
    correct = 0
    for line in parse:
        cards = line.split()[:10]
        hand1 = cards[:5]
        hand2 = cards[5:]
        win = winner(hand1, hand2)
        if win == answer[counter]:
            correct = correct + 1
        else:
            print cards
            print "You said that " + str(win) + " won, but the winner is " + str(3 - win)
        counter = counter + 1
    return correct

print "Running flush tests"
print str(flushtest()) + " out of 10 tests passed for flush code!"
print "Running straight tests"
print str(straighttest()) + " out of 10 tests passed for straight code!"
print "Running rank tests"
print str(ranktest()) + " out of 10 tests passed for rank code!"
print "Running winner tests"
print str(winnertest()) + " out of 1000 tests passed for winner code!"
