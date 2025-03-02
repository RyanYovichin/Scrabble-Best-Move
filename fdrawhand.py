import random
def drawhand(hand,bag):
    for i in range (7-len(hand)):
        letternum = random.randint(0, len(bag) - 1)
        letter=bag[letternum]
        hand.append(letter)
        bag.remove(letter)
        #print(letter)
    #print(hand)
    return hand