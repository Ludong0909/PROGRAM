# poker score

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


def score(deck, suit, rank):
    score = 0

    # Rule A (Aces)
    for i in range(5):
        if deck[i].rank == 'A':
            score += 5

    # Rule B (Pairs)
    n = 0
    for i in range(5):
        for j in range(i+1, 5):
            if deck[i].rank == deck[j].rank:
                score += 10
                n += 1
    # Rule E (Full House)
    if n == 4:
        score += 80
    # Rule F (Four of a kind)
    if n == 6:
        score += 100
    # impossible condition (Five same rank, got 5 * points by Rule F)
    if n == 10:
        score += 500

    # Rule C (Flush)
    if len(set(suit)) == 1:
        score += 30

    # Rule D (Straight)
    straight = list('A23456789') + ['10'] + list('JQKA234')
    for i in range(13):
        if set(straight[i:i+5]) == set(rank):
            score += 50
            # Rule G (Flush Straight)
            if len(set(suit)) == 1:
                score += 300
            break
    return score


suit = input().split(',')
rank = input().split(',')
deck = [0] * 5

for i in range(5):
    deck[i] = Card(suit[i], rank[i])

print(score(deck, suit, rank))
