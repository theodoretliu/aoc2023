with open("d03.txt", "r") as f:
    grid = []
    for l in f:
        grid.append(list(l.strip()))

    s = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "*":
                adjacent_nums = []
                grid_copy = [row[:] for row in grid]

                for x, y in [
                    [0, 1],
                    [0, -1],
                    [-1, 0],
                    [-1, -1],
                    [-1, 1],
                    [1, 1],
                    [1, 0],
                    [1, -1],
                ]:
                    new_x, new_y = i + x, j + y

                    if (
                        0 <= new_x < len(grid)
                        and 0 <= new_y < len(grid[0])
                        and grid[new_x][new_y] in "1234567890"
                    ):
                        left_bound = new_y
                        right_bound = new_y

                        while (
                            left_bound >= 0 and grid[new_x][left_bound] in "1234567890"
                        ):
                            left_bound -= 1

                        while (
                            right_bound < len(grid[0])
                            and grid[new_x][right_bound] in "1234567890"
                        ):
                            right_bound += 1

                        num = int("".join(grid[new_x][left_bound + 1 : right_bound]))
                        adjacent_nums.append(num)

                        for k in range(left_bound + 1, right_bound):
                            grid[new_x][k] = "."

                if len(adjacent_nums) == 2:
                    p = 1

                    for num in adjacent_nums:
                        p *= num
                    s += p

                grid = grid_copy
    print(s)
