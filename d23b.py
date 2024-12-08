grid = []
with open("d23.txt", "r") as f:
    for line in f:
        grid.append(line.strip())


delta_m = {"^": (-1, 0), ">": (0, 1), "<": (0, -1), "v": (1, 0)}
valid = "." + "".join(delta_m.keys())
important_vertices = set([(0, 1), (len(grid) - 1, len(grid[0]) - 2)])

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] not in valid:
            continue

        if (i, j) in important_vertices:
            continue

        c = 0
        for dx, dy in delta_m.values():
            newx, newy = i + dx, j + dy

            if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]):
                c += grid[newx][newy] in valid

        if c in (1, 3, 4):
            important_vertices.add((i, j))


def get_step(i, j, previ, prevj):
    assert (i, j) not in important_vertices, (i, j)

    for dx, dy in delta_m.values():
        newx, newy = i + dx, j + dy

        if (
            0 <= newx < len(grid)
            and 0 <= newy < len(grid[0])
            and grid[newx][newy] in valid
            and (newx, newy) != (previ, prevj)
        ):
            return newx, newy

    assert False, (i, j, previ, prevj)


from collections import defaultdict

g = defaultdict(dict)

q = [(0, 1, {(0, 1)})]


while len(q) > 0:
    i, j, visited = q.pop(0)

    for dx, dy in delta_m.values():
        newx, newy = i + dx, j + dy

        if (
            0 <= newx < len(grid)
            and 0 <= newy < len(grid[0])
            and grid[newx][newy] in valid
        ):
            prevx, prevy = i, j
            c = 1
            while (newx, newy) not in important_vertices:
                c += 1
                (prevx, prevy), (newx, newy) = (newx, newy), get_step(
                    newx, newy, prevx, prevy
                )

            if (newx, newy) not in visited:
                g[(i, j)][(newx, newy)] = c

                q.append((newx, newy, visited | {(newx, newy)}))


print(g)
exit(0)

# q = [(0, 1)]
# print(len(important_vertices))

# exit(0)

visited = set()


q = [(0, 1, {(0, 1)})]

longest = -float("inf")

while len(q) > 0:
    i, j, visited = q.pop(-1)
    curr = grid[i][j]

    if curr == "#":
        continue

    if i == len(grid) - 1 and j == len(grid[0]) - 2:
        longest = max(longest, len(visited))
        continue

    # if curr in "<>^v":
    #     dx, dy = delta_m[curr]

    #     nx, ny = i + dx, j + dy

    #     if (nx, ny) not in visited:
    #         q.append((nx, ny, visited | {(nx, ny)}))

    #     continue

    for dx, dy in delta_m.values():
        nx, ny = i + dx, j + dy

        if (
            (nx, ny) not in visited
            and 0 <= i < len(grid)
            and 0 <= j < len(grid[0])
            and grid[i][j] != "#"
        ):
            q.append((nx, ny, visited | {(nx, ny)}))


print(longest - 1)
