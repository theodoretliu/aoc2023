with open("d04.txt", "r") as f:
    s = 0
    s2 = 0
    copies = [1] * 214
    for i, l in enumerate(f):
        num, rest = l.split(":")

        winning, hand = rest.split("|")

        hand = hand.strip()

        winning = winning.strip().split()
        cards_in_hand = hand.split()

        copies_of_current = copies[i]
        score = 0
        copies_of_next = 0
        for card in cards_in_hand:
            if card in winning:
                copies_of_next += 1
                if score >= 1:
                    score *= 2
                else:
                    score += 1

        for j in range(copies_of_next):
            copies[i + j + 1] += copies_of_current

        s += score
        s2 += score * copies[i]

    print(sum(copies))
