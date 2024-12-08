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


def evaluate(workflow, avail):
    label, rules, final = workflow

    res =a
    for ax in avail:
        for letter, cmp, val, dest in rules:





workflows = [parse_workflow(s) for s in workflow_s]
workflow_dict = {workflow[0]: workflow for workflow in workflows}

queue = [
    (
        workflow_dict["in"],
        [{"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)}],
    )
]

accepted = []

while len(queue) > 0:
    cur_workflow, avails = queue.pop(0)

    for avail in avails:
        new_splits = evaluate(cur_workflow, avail)
        queue.append(new_splits)


tot = 0
for a in accepted:
    s = 1
    for lower, upper in a.values():
        s *= upper - lower
    tot += s
