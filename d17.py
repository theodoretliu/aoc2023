grid = []
with open("d17.txt", "r") as f:
    for l in f:
        row = [int(c) for c in l.strip()]
        grid.append(row)

opp = {"D": "U", "U": "D", "L": "R", "R": "L"}

deltas = {"D": (1, 0), "U": (-1, 0), "L": (0, -1), "R": (0, 1)}

visited = {}


cache = {}


def shortest_path(x, y, count, prev_dir, cache, new_cache, available_steps):
    if x == len(grid) - 1 and y == len(grid[0]) - 1:
        new_cache[(x, y, count, prev_dir)] = 0
        return 0

    if available_steps == 0:
        new_cache[(x, y, count, prev_dir)] = float("inf")

        return float("inf")

    print(x, y, prev_dir, available_steps)
    avail = []

    for direction, (delta_x, delta_y) in deltas.items():
        new_x, new_y = x + delta_x, y + delta_y

        if not (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])):
            continue

        if prev_dir == direction and count < 3:
            avail.append(
                grid[new_x][new_y] + cache[(new_x, new_y, count + 1, direction)]
            )
        elif prev_dir != direction and prev_dir != opp[direction]:
            avail.append(grid[new_x][new_y] + cache[(new_x, new_y, 1, direction)])

    new_cache[(x, y, count, prev_dir)] = min(avail)
    return min(avail)


cache = {}

for x in range(len(grid)):
    for y in range(len(grid[0])):
        for prev_dir in deltas.keys():
            for count in range(4):
                if x == len(grid) - 1 and y == len(grid[0]) - 1:
                    cache[(x, y, prev_dir, count)] = 0
                else:
                    cache[(x, y, prev_dir, count)] = float("inf")

allowed_visits = len(grid) * len(grid[0])
for i in range(allowed_visits - 1):
    new_cache = {}
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for prev_dir in deltas.keys():
                for count in range(4):
                    if x == len(grid) - 1 and y == len(grid[0]) - 1:
                        new_cache[(x, y, prev_dir, count)] = 0
                        continue

                    avail = []

                    for direction, (delta_x, delta_y) in deltas.items():
                        new_x, new_y = x + delta_x, y + delta_y

                        if not (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])):
                            continue

                        if prev_dir == direction and count < 3:
                            avail.append(
                                grid[new_x][new_y]
                                + cache[(new_x, new_y, direction, count + 1)]
                            )
                        elif prev_dir != direction and prev_dir != opp[direction]:
                            avail.append(
                                grid[new_x][new_y] + cache[(new_x, new_y, direction, 1)]
                            )

                    new_cache[(x, y, prev_dir, count)] = min(avail)

    cache = new_cache
    print(new_cache[(0, 0, "D", 0)])
