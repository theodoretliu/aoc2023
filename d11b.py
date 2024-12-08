with open("d11.txt", "r") as f:
    s = 0
    galaxy_pairs = []
    world = []
    for i, l in enumerate(f):
        x = l.strip()
        world.append(list(x))

    empty_rows = []
    for i, row in enumerate(world):
        if not any(c == "#" for c in row):
            empty_rows.append(i)

    empty_cols = []
    for i in range(len(world[0])):
        col = [row[i] for row in world]

        if not any(c == "#" for c in col):
            empty_cols.append(i)

    print(empty_rows, empty_cols)

    for i, row in enumerate(world):
        for j, c in enumerate(row):
            if c == "#":
                galaxy_pairs.append((i, j))

    s = 0
    for i in range(len(galaxy_pairs) - 1):
        for j in range(i + 1, len(galaxy_pairs)):
            (a, b), (c, d) = galaxy_pairs[i], galaxy_pairs[j]

            a, c = min(a, c), max(a, c)
            b, d = min(b, d), max(b, d)

            dist = 0
            for k in range(a, c):
                if k in empty_rows:
                    dist += 10**6
                else:
                    dist += 1

            for k in range(b, d):
                if k in empty_cols:
                    dist += 10**6
                else:
                    dist += 1

            s += dist

    print(s)
