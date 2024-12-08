grid = []
with open("d10.txt", "r") as f:
    for l in f:
        grid.append(list(l.strip()))

starting_position = None
m = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, -1), (1, 0)],
    "F": [(0, 1), (1, 0)],
}

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            starting_position = (i, j)

dist = 0

x, y = starting_position
visited = set([starting_position, (x - 1, y), (x, y + 1)])

frontier = [(x - 1, y), (x, y + 1)]

dist += 1
while len(frontier) > 0:
    new_frontier = []

    for x, y in frontier:
        for dx, dy in m[grid[x][y]]:
            new_x, new_y = x + dx, y + dy

            if (new_x, new_y) not in visited:
                new_frontier.append((new_x, new_y))
                visited.add((new_x, new_y))

    frontier = new_frontier

    dist += 1

print(dist - 1)


grid_distances = []
