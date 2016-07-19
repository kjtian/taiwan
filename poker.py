# --------------------------------------PROBLEM 1--------------------------------------

# Take a hand and determine if it is a flush or not
# Ex. flush(["TD", "AD", "QD", "2D", "5D"]) should be True
# Ex. flush(["2H", "5H", "4H", "AD", "AC"]) should be False

def flush(hand):
    # TODO: Write code! (Delete the next line)
    pass

# --------------------------------------PROBLEM 2--------------------------------------

# Take a hand and determine if it is a straight or not
# Ex. straight(["AC", "4H", "2C", "5D", "3C"]) should be True
# Ex. straight(["6C", "8C", "7C", "9D", "JD"]) should be False

def straight(hand):
    # TODO: Write code! (Delete the next line)
    pass

# --------------------------------------PROBLEM 3--------------------------------------

# Take a hand and determine its rank.
# Ex. rank(["4C", "AS", "JS", "9S", "7C"]) should be 0
# Ex. rank(["4C", "4D", "4S", "4H", "5H"]) should be 7
# 0 high card 1 one pair 2 two pairs 3 triple 4 straight
# 5 flush 6 full house 7 four of a kind 8 straight flush

def rank(hand):
    if straight(hand) and flush(hand):
        return 8
    # TODO: Write code!

# THIS MIGHT BE HELPFUL???
def counts(hand):
    cards = []
    counts = []
    for card in hand:
        if convert(card[0]) not in cards:
            cards.append(convert(card[0]))
            counts.append(1)
        else:
            counts[cards.index(convert(card[0]))] = counts[cards.index(convert(card[0]))] + 1
    return cards, counts

# --------------------------------------PROBLEM 4--------------------------------------

# Take two hands and return either 1 or 2, depending on if player 1 or player 2 wins.
# Ex. winner(["4C", "AS", "JS", "9S", "7C"], ["TS", "7H", "9H", "JC", "KS"]) should be 1.

def winner(hand1, hand2):
    # TODO: Write code!
    pass
    
