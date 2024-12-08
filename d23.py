grid = []
with open("d23.txt", "r") as f:
    for line in f:
        grid.append(line.strip())


visited = set()


delta_m = {"^": (-1, 0), ">": (0, 1), "<": (0, -1), "v": (1, 0)}


def longest_f(i, j):
    print(i, j)
    if (i, j) in visited:
        return -float("inf")

    if not (0 <= i < len(grid)):
        return -float("inf")

    if not (0 <= j < len(grid[0])):
        return -float("inf")

    if i == len(grid) - 1 and j == len(grid[0]) - 2:
        return 1

    curr = grid[i][j]

    if curr == "#":
        return -float("inf")

    if curr in "^><v":
        dx, dy = delta_m[curr]
        next_i, next_j = i + dx, j + dy
        visited.add((i, j))
        l = 1 + longest(next_i, next_j)
        visited.remove((i, j))

        return l

    res = []

    visited.add((i, j))
    for dx, dy in delta_m.values():
        next_i, next_j = i + dx, j + dy
        res.append(longest(next_i, next_j))

    visited.remove((i, j))

    l = 1 + max(res)

    return l


q = [(0, 1, {(0, 1)})]

longest = -float("inf")

while len(q) > 0:
    i, j, visited = q.pop(0)
    curr = grid[i][j]

    if curr == "#":
        continue

    if not (0 <= i < len(grid)):
        continue

    if not (0 <= j < len(grid[0])):
        continue

    if i == len(grid) - 1 and j == len(grid[0]) - 2:
        longest = max(longest, len(visited))
        continue

    if curr in "<>^v":
        dx, dy = delta_m[curr]

        nx, ny = i + dx, j + dy

        if (nx, ny) not in visited:
            q.append((nx, ny, visited | {(nx, ny)}))

        continue

    for dx, dy in delta_m.values():
        nx, ny = i + dx, j + dy

        if (nx, ny) not in visited:
            q.append((nx, ny, visited | {(nx, ny)}))


print(longest - 1)
