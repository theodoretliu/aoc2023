grid = []
with open("d14.txt", "r") as f:
    for l in f:
        grid.append(list(l.strip()))


def th(g):
    return tuple(tuple(row) for row in g)


def cload(g):
    load = 0

    for i, row in enumerate(g):
        for c in row:
            if c == "O":
                load += len(g) - i

    return load


states = [th(grid)]
prev_states = set(states)
loads = [cload(grid)]

for _ in range(10**9):
    # tilt north
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            r = j
            while r >= 1 and grid[r][i] == "O" and grid[r - 1][i] == ".":
                grid[r][i], grid[r - 1][i] = ".", "O"
                r -= 1

    # tilt west
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            c = j
            while c >= 1 and grid[i][c] == "O" and grid[i][c - 1] == ".":
                grid[i][c], grid[i][c - 1] = ".", "O"
                c -= 1

    # tilt south
    for i in range(len(grid[0])):
        for j in range(len(grid) - 1, -1, -1):
            r = j
            while (
                r < len(grid)
                and r + 1 < len(grid)
                and grid[r][i] == "O"
                and grid[r + 1][i] == "."
            ):
                grid[r][i], grid[r + 1][i] = ".", "O"
                r += 1

    # tilt east
    for i in range(len(grid)):
        for j in range(len(grid[0]) - 1, -1, -1):
            c = j
            while (
                c < len(grid[0])
                and c + 1 < len(grid[0])
                and grid[i][c] == "O"
                and grid[i][c + 1] == "."
            ):
                grid[i][c], grid[i][c + 1] = ".", "O"
                c += 1

    # for row in grid:
    #     print("".join(row))
    hashed = th(grid)

    if hashed in prev_states:
        break

    states.append(hashed)
    prev_states.add(hashed)
    loads.append(cload(grid))


cycle_start = states.index(hashed)
cycle_length = len(loads) - cycle_start

whereincycle = (10**9 - cycle_start) % cycle_length

print(loads[cycle_start + whereincycle])
