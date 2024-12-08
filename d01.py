nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}

from collections import defaultdict

with open("d01.txt", "r") as f:
    s = 0
    second = 0
    for l in f:
        n = [x for x in l if x in "0123456789"]

        d = defaultdict()

        first_num = None
        for i in range(len(l)):
            if l[i] in "1234567890":
                first_num = l[i]
                break

            for num, val in nums.items():
                if l[i : i + len(num)] == num:
                    first_num = str(val)
                    break

            if first_num is not None:
                break

        last_num = None
        for j in range(len(l) - 1, -1, -1):
            if l[j] in "1234567890":
                last_num = l[j]
                break

            for num, val in nums.items():
                if l[j : j + len(num)] == num:
                    last_num = str(val)
                    break

            if last_num is not None:
                break

        second += int(first_num + last_num)

        y = n[0] + n[-1]
        s += int(y)

    print(s)
    print(second)
