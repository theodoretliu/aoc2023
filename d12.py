cache = {}


def solve(springs, arr):
    if len(arr) == 0:
        return all(x in ("?", ".") for x in springs)

    if len(springs) == 0:
        return 0

    cur = arr[0]

    if len(springs) < cur:
        return 0

    if len(springs) == cur:
        if all(x in ("?", "#") for x in springs[:cur]):
            assert len(springs[cur:]) == 0
            return solve(springs[cur:], arr[1:])

        return 0

    res = 0
    if all(x in ("?", "#") for x in springs[:cur]) and springs[cur] in (
        "?",
        ".",
    ):
        res += solve(springs[cur + 1 :], arr[1:])

    if springs[0] in ("?", "."):
        res += solve(springs[1:], arr)

    return res


def generate(arr, length):
    if len(arr) == 0:
        return ["." * length]

    if length < 0:
        return []

    first = arr[0]

    if first > length:
        return []

    if first == length:
        return ["#" * first + x for x in generate(arr[1:], length - first)]

    res = []
    res.extend("." + x for x in generate(arr, length - 1))
    res.extend("#" * first + "." + x for x in generate(arr[1:], length - first - 1))

    return res


def check(unknown, gend):
    assert len(unknown) == len(gend)

    for x, y in zip(unknown, gend):
        if not (x == y or x == "?"):
            return False

    return True


def naive(springs, arr):
    count = 0
    for possible in generate(arr, len(springs)):
        count += check(springs, possible)

    return count


s = 0
with open("d12.txt", "r") as f:
    for l in f:
        springs, arr = l.strip().split()
        arr = [int(x) for x in arr.split(",")]
        res = solve(springs, arr)
        s += res


print(s)

# print(generate([1, 3, 1], 10))
