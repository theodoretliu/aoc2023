with open("d19.txt", "r") as f:
    x = None
    workflow_s = []
    while len(x := f.readline().strip()) > 0:
        workflow_s.append(x)

    parts = []
    for l in f:
        parts.append(l.strip())

import re


def parse_workflow(s):
    res = re.match(r"([a-z]*)\{(.*)\}", s)

    label, inner = res.group(1), res.group(2)

    pairs = inner.split(",")

    rules = []
    for pair in pairs[:-1]:
        res = re.match(r"([xmas])(>|<)(\d+):(.+)", pair)

        rules.append([res.group(1), res.group(2), int(res.group(3)), res.group(4)])

    return label, rules, pairs[-1]


workflows = [parse_workflow(s) for s in workflow_s]
workflow_dict = {workflow[0]: workflow for workflow in workflows}
s2 = 0

for part in parts:
    res = re.match(r"\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}", part)
    x, m, a, s = [int(res.group(y)) for y in range(1, 5)]
    v = {"x": x, "m": m, "a": a, "s": s}

    cur = workflow_dict["in"]
    accepted = None
    while True:
        new_dest = None
        for key, cmp, val, dest in cur[1]:
            if cmp == ">" and v[key] > val:
                new_dest = dest
                break

            if cmp == "<" and v[key] < val:
                new_dest = dest
                break

        if new_dest is None:
            new_dest = cur[2]

        if new_dest in ("A", "R"):
            accepted = new_dest == "A"
            break

        cur = workflow_dict[new_dest]

    if accepted:
        s2 += sum(v.values())

print(s2)
