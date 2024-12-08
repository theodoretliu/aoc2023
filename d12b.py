cache = {}


def solve(springs_t, arr_t, i, j):
    if (springs_t, arr_t, i, j) in cache:
        return cache[(springs_t, arr_t, i, j)]

    if j == len(arr_t):
        return all(x in ("?", ".") for x in springs_t[i:])

    if i == len(springs_t):
        return 0

    cur = arr_t[j]

    if len(springs_t) - i < cur:
        return 0

    if len(springs_t) - i == cur:
        if all(x in ("?", "#") for x in springs_t[i : i + cur]):
            return solve(springs_t, arr_t, i + cur, j + 1)

        return 0

    res = 0
    if all(x in ("?", "#") for x in springs_t[i : i + cur]) and springs_t[i + cur] in (
        "?",
        ".",
    ):
        res += solve(springs_t, arr_t, i + cur + 1, j + 1)

    if springs_t[i] in ("?", "."):
        res += solve(springs_t, arr_t, i + 1, j)

    cache[(springs_t, arr_t, i, j)] = res

    return res


s = 0
with open("d12.txt", "r") as f:
    for l in f:
        springs, arr = l.strip().split()
        arr = [int(x) for x in arr.split(",")]
        res2 = solve("?".join([springs] * 5), tuple(arr * 5), 0, 0)

        s += res2

print(s)

# print(generate([1, 3, 1], 10))
