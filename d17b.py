grid = []
with open("d17.txt", "r") as f:
    for l in f:
        row = [int(c) for c in l.strip()]
        grid.append(row)

opp = {"D": "U", "U": "D", "L": "R", "R": "L"}

deltas = {"D": (1, 0), "U": (-1, 0), "L": (0, -1), "R": (0, 1)}

visited = {}


cache = {}


cache = {}

for x in range(len(grid)):
    for y in range(len(grid[0])):
        for prev_dir in deltas.keys():
            for count in range(11):
                if x == len(grid) - 1 and y == len(grid[0]) - 1 and count >= 4:
                    cache[(x, y, prev_dir, count)] = 0
                else:
                    cache[(x, y, prev_dir, count)] = float("inf")

allowed_visits = len(grid) * len(grid[0])
for i in range(allowed_visits - 1):
    new_cache = {}
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for prev_dir in deltas.keys():
                for count in range(11):
                    if x == len(grid) - 1 and y == len(grid[0]) - 1 and count >= 4:
                        new_cache[(x, y, prev_dir, count)] = 0
                        continue

                    if count < 4:
                        delta_x, delta_y = deltas[prev_dir]
                        new_x, new_y = x + delta_x, y + delta_y

                        if not (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])):
                            new_cache[(x, y, prev_dir, count)] = float("inf")
                            continue
                        else:
                            new_cache[(x, y, prev_dir, count)] = (
                                grid[new_x][new_y]
                                + cache[(new_x, new_y, prev_dir, count + 1)]
                            )
                            continue

                    avail = []

                    for direction, (delta_x, delta_y) in deltas.items():
                        new_x, new_y = x + delta_x, y + delta_y

                        if not (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])):
                            continue

                        if prev_dir == direction and count < 10:
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
    print(i, new_cache[(0, 0, "D", 0)], new_cache[(0, 0, "R", 0)])
