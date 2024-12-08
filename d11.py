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

    inc = 0
    for i in empty_rows:
        world.insert(i + inc, ["."] * len(world[0]))
        inc += 1

    inc = 0
    for i in empty_cols:
        for row in world:
            row.insert(i + inc, ".")

        inc += 1

    for i, row in enumerate(world):
        for j, c in enumerate(row):
            if c == "#":
                galaxy_pairs.append((i, j))

    s = 0
    for i in range(len(galaxy_pairs) - 1):
        for j in range(i + 1, len(galaxy_pairs)):
            (a, b), (c, d) = galaxy_pairs[i], galaxy_pairs[j]

            s += abs(c - a) + abs(d - b)

    print(s)
