def solve(seq):
    if all(s == 0 for s in seq):
        return 0

    return seq[-1] + solve([seq[i] - seq[i - 1] for i in range(1, len(seq))])


s = 0
with open("d09.txt", "r") as f:
    for l in f:
        seq = [int(x) for x in l.strip().split()]

        s += solve(seq)

print(s)
