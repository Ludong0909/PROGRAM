# Hw8 for PBC
# Created on 20230514 by Tsai,C,Y
# Q2------------------------------------------------------------
# define class Card
class Card:

    def __init__(self, shape, number):
        self.shape = shape
        self.number = number

    def isAce(self):
        if self.number == 1:
            return True
        else:
            return False
        
    def isPair(self, another_card):  # another_card is a class Card
        if self.number == another_card.number:
            return True
        else:
            return False


# define global functions
def flush(deck):
    # check if all cards have the same shape
    shapes = set([card.shape for card in deck])
    return len(shapes) == 1


def straight(deck):
    # check if all cards have consecutive numbers, considering the case where the number sequence crosses the end
    numbers = sorted([card.number for card in deck])
    if numbers == [1, 10, 11, 12, 13]:
        return True
    elif numbers == [1, 2, 3, 4, 13]:
        return True
    elif numbers == [1, 2, 11, 12, 13]:
        return True
    elif numbers == [1, 2, 3, 12, 13]:
        return True
    elif numbers == [1, 2, 3, 4, 13]:
        return True
    else:
        return numbers == list(range(min(numbers), max(numbers)+1))


def fullhouse(deck):
    # check if there are three cards with the same number and two cards with the same number
    numbers = [card.number for card in deck]
    for num in set(numbers):
        if numbers.count(num) >= 2:
            for num2 in set(numbers):
                if num2 != num and numbers.count(num2) >= 3:
                    return True
    return False


def four_of_a_kind(deck):
    # check if there are four cards with the same number
    numbers = [card.number for card in deck]
    for num in set(numbers):
        if numbers.count(num) >= 4:
            return True
    return False


def five_of_a_kind(deck):  # special condition
    # check if there are four cards with the same number
    numbers = [card.number for card in deck]
    for num in set(numbers):
        if numbers.count(num) == 5:
            return True
    return False


def straight_flush(deck):
    # check if all cards have the same shape and consecutive numbers
    if flush(deck) and straight(deck):
        return True
    return False


# read input
n = int(input())
Score = []
for i in range(n):
    line = input().split(',')
    shape = []
    number = []
    for j in range(5):
        shape.append(line[j][0])
        number.append((line[j][1:]))

    for i in range(5):
        if number[i] == 'A':
            number[i] = 1
        elif number[i] == 'J':
            number[i] = 11
        elif number[i] == 'Q':
            number[i] = 12
        elif number[i] == 'K':
            number[i] = 13
        else:
            number[i] = int(number[i])

    # creat deck
    c0 = Card(shape[0], number[0])
    c1 = Card(shape[1], number[1])
    c2 = Card(shape[2], number[2])
    c3 = Card(shape[3], number[3])
    c4 = Card(shape[4], number[4])
    deck = [c0, c1, c2, c3, c4] 

    # calculating score
    # initialize
    score = 0

    # calculationg
    for card in deck:

        # check Ace
        if card.isAce():
            score += 5

        # check pair
        for another_card in deck:
            if another_card != card:
                if another_card.isPair(card):
                    score += 5  # C^n_2
        
    # check flush
    if flush(deck):
        score += 30

    # check straight
    if straight(deck):
        score += 50

    # check fullhouse
    if fullhouse(deck):
        score += 80

    # check four of a kind and special
    if four_of_a_kind(deck):
        score += 100
    if five_of_a_kind(deck):  # if five of a kind, extra 400 pts
        score += 400

    # check straight flush
    if straight_flush(deck):
        score += 300

    Score.append(float(score))

Max = max(Score)
out = []
for i in range(len(Score)):
    if Score[i] == Max:
        out.append(i+1)

print(*out, sep=',')