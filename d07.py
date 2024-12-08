cards = []
with open("d07.txt", "r") as f:
    for l in f:
        hand, score = l.strip().split()
        cards.append((hand, score))

m = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

m2 = [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]

from collections import Counter
from functools import cmp_to_key


def compare(card1, card2):
    (hand1, _), (hand2, _) = card1, card2

    h1 = [int(x) if x not in m else m[x] for x in hand1]
    h2 = [int(x) if x not in m else m[x] for x in hand2]

    c1 = Counter(h1)
    c2 = Counter(h2)

    counts1 = tuple(sorted(c1.values(), reverse=True))
    counts2 = tuple(sorted(c2.values(), reverse=True))

    cv1 = m2.index(counts1)
    cv2 = m2.index(counts2)

    if cv1 < cv2:
        return 1

    if cv1 > cv2:
        return -1

    for x1, x2 in zip(h1, h2):
        if x1 > x2:
            return 1

        if x1 < x2:
            return -1

    print(card1, card2)
    raise Exception("shouldn't reach")


def compare2(card1, card2):
    (hand1, _), (hand2, _) = card1, card2

    h1 = [int(x) if x not in m else m[x] for x in hand1]
    h2 = [int(x) if x not in m else m[x] for x in hand2]

    c1 = Counter(h1)
    c2 = Counter(h2)

    counts1 = tuple(sorted(c1.values(), reverse=True))
    counts2 = tuple(sorted(c2.values(), reverse=True))

    cv1 = m2.index(counts1)
    cv2 = m2.index(counts2)

    if cv1 < cv2:
        return 1

    if cv1 > cv2:
        return -1

    for x1, x2 in zip(h1, h2):
        if x1 > x2:
            return 1

        if x1 < x2:
            return -1

    print(card1, card2)
    raise Exception("shouldn't reach")
def compare2


cards = sorted(cards, key=cmp_to_key(compare))

s = 0

for i, (_, wager) in enumerate(cards):
    s += (i + 1) * int(wager)

print(s)
