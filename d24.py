lines = []
with open("d24.txt", "r") as f:
    for l in f:
        left, right = l.strip().split("@")
        left = [int(x.strip()) for x in left.strip().split(",")]
        right = [int(x.strip()) for x in right.strip().split(",")]

        lines.append((tuple(left), tuple(right)))

from fractions import Fraction


def intersection(x, y, dx, dy, x2, y2, dx2, dy2):
    slope1, slope2 = Fraction(dy, dx), Fraction(dy2, dx2)

    if slope1 == slope2:
        return None

    sol_x = (-slope2 * x2 - y + slope1 * x + y2) / (slope1 - slope2)
    sol_y = slope1 * (sol_x - x) + y

    t1 = Fraction(sol_y - y, dy)
    t2 = Fraction(sol_y - y2, dy2)

    return sol_x, sol_y, t1, t2


LOWER = 200000000000000
UPPER = 400000000000000
count = 0
for i in range(len(lines) - 1):
    for j in range(i + 1, len(lines)):
        ((x, y, _), (dx, dy, _)), ((x2, y2, _), (dx2, dy2, _)) = lines[i], lines[j]

        inter = intersection(x, y, dx, dy, x2, y2, dx2, dy2)

        if inter is None:
            continue

        x, y, t1, t2 = inter

        if LOWER <= x <= UPPER and LOWER <= y <= UPPER and t1 >= 0 and t2 >= 0:
            count += 1


print(count)
