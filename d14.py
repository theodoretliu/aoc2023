grid = []
with open("d14.txt", "r") as f:
    for l in f:
        grid.append(list(l.strip()))

for i in range(len(grid[0])):
    for j in range(len(grid)):
        r = j
        while r >= 1 and grid[r][i] == "O" and grid[r - 1][i] == ".":
            grid[r][i], grid[r - 1][i] = ".", "O"
            r -= 1

load = 0

for i, row in enumerate(grid):
    for c in row:
        if c == "O":
            load += len(grid) - i


for row in grid:
    print("".join(row))

print(load)
