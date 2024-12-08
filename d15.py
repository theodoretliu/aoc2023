import re


def hash(step):
    cur = 0
    for c in step:
        cur += ord(c)
        cur *= 17
        cur %= 256

    return cur


def box_find(box, label):
    for i, (l, _) in enumerate(box):
        if l == label:
            return i

    return -1


with open("d15.txt", "r") as f:
    full = f.readline().strip()

    steps = full.split(",")

    s = 0
    for step in steps:
        cur = 0
        for c in step:
            cur += ord(c)
            cur *= 17
            cur %= 256

        s += cur

    print(s)
    boxes = [[] for _ in range(256)]

    for i, step in enumerate(steps):
        label = re.match(r"([A-Za-z])+", step).group(0)
        box_id = hash(label)

        box = boxes[box_id]

        idx = box_find(box, label)

        if step[-1] == "-" and idx >= 0:
            del box[idx]

        elif step[-1] != "-":
            power = int(step[-1])
            if idx >= 0:
                box[idx] = (label, power)
            else:
                box.append((label, power))

    s2 = 0
    for j, box in enumerate(boxes):
        p = 0
        for i, (_, power) in enumerate(box):
            p += (j + 1) * (i + 1) * power

        s2 += p

    print(s2)
