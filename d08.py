import re

with open("d08.txt", "r") as f:
    first = f.readline().strip()
    f.readline()

    s = []
    m = {}
    for l in f:
        match = re.match(r"(.*) = \((.*), (.*)\)", l.strip())
        x, l, r = match.group(1), match.group(2), match.group(3)

        m[x] = (l, r)

idx = 0
first = first.strip()
pos = "AAA"
steps = 0
while True:
    l, r = m[pos]

    if first[idx] == "L":
        pos = l
    else:
        pos = r

    steps += 1

    if pos == "ZZZ":
        break

    idx += 1

    if idx == len(first):
        idx = 0

print(steps)
