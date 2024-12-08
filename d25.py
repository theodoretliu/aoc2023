from collections import defaultdict

graph = defaultdict(dict)

with open("d25.txt", "r") as f:
    for l in f:
        node, neighbors = l.strip().split(":")

        node = node.strip()

        neighbors = [x.strip() for x in neighbors.split()]

        for neighbor in neighbors:
            graph[(node,)][(neighbor,)] = 1
            graph[(neighbor,)][(node,)] = 1


def compact(g, s, t):
    combined = tuple(sorted(s + t))

    del g[s]
    del g[t]
    g[combined] = dict()
    for v in g:
        if s in g[v] or t in g[v]:
            result_weight = 0
            if s in g[v]:
                result_weight += g[v][s]
                del g[v][s]
            if t in g[v]:
                result_weight += g[v][t]
                del g[v][t]

            g[v][combined] = result_weight
            g[combined][v] = result_weight


def min_cut_phase(g):
    t = list(g.keys())[0]
    s = None
    a = set([t])

    avail_choose = set(g.keys()) - a

    while len(a) < len(g):
        num_connects = -float("inf")
        best = None
        for vertex in avail_choose:
            temp = sum(g[vertex][y] for y in g[vertex] if y in a)
            if temp > num_connects:
                num_connects = temp
                best = vertex

        s, t = t, best

        a.add(best)
        avail_choose.remove(best)

    min_cut_candidate = set()
    for v in g[t]:
        for v_sub in v:
            for t_sub in t:
                min_cut_candidate.add(tuple(sorted((v_sub, t_sub))))

    min_cut_size = 0
    for v in g[t]:
        min_cut_size += g[t][v]

    combined = tuple(sorted(s + t))

    # if "hfx" in t:
    #     print(g, s, t)
    #     exit(0)

    compact(g, s, t)

    return min_cut_size, len(t)


def min_cut(g):
    min_cut = float("inf")
    edge_set = None

    while len(g) > 2:
        print(len(g))
        size, edge_set_candidate = min_cut_phase(g)
        # break

        # print(size, edge_set_candidate)

        if size < min_cut:
            min_cut = size
            edge_set = edge_set_candidate

    return min_cut, edge_set


orig_g = len(graph)
size, edges = min_cut(graph)
print(edges * (orig_g - edges))
print(size, edges)


# print(graph)
# compact(graph, ("a",), ("d",))
# print(graph)

# compact(graph, ("c",), ("b",))
# print(graph)
# compact(graph, ("b", "c"), ("e",))
# print(graph)
