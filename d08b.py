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

poses = [x for x in m.keys() if x[-1] == "A"]
idx = 0
first = first.strip()
steps = 0
# print(first)

all_periods = []


for pos in poses:
    idx = 0

    periods = []

    visited = set([(pos, idx)])
    curr = pos
    steps = 0

    while True:
        l, r = m[curr]

        if first[idx] == "L":
            curr = l
        else:
            curr = r

        steps += 1

        idx += 1
        if idx == len(first):
            idx = 0

        if curr[-1] == "Z":
            periods.append(steps)

        if (curr, idx) in visited:
            break

        visited.add((curr, idx))

    all_periods.append(periods)

print(",".join(str(y) for x in all_periods for y in x))  # get the LCM of this
