def does_intersect(pair1, pair2):
    (start1, length1), (start2, length2) = pair1, pair2

    if start2 + length2 <= start1:
        return None

    if start1 + length1 <= start2:
        return None

    if start2 <= start1:
        left = start1

        right = min(start1 + length1, start2 + length2)
        remaining = start1 + length1 - right

        # assert right - left + remaining == length1
        return [left, right - left], [[right, remaining]]

    left = start2
    right = min(start1 + length1, start2 + length2)
    remaining = start1 + length1 - right

    # assert right - left + remaining == length1, (pair1, pair2)
    return [left, right - left], [[start1, start2 - start1], [right, remaining]]


with open("d05.txt", "r") as f:
    seeds = f.readline()
    _, seeds = seeds.strip().split(":")
    seeds = [int(seed) for seed in seeds.split()]

    seed_pairs = [[seeds[i], seeds[i + 1]] for i in range(0, len(seeds), 2)]

    f.readline()

    maps = []

    for _ in range(7):
        f.readline()  # name of the map
        current_map = []

        while len((line := f.readline().strip())) > 0:
            start1, start2, length = line.strip().split()
            current_map.append((int(start1), int(start2), int(length)))

        maps.append(current_map)

    print(seed_pairs)
    minn = float("inf")

    for start, pair_length in seed_pairs:
        q = [(start, pair_length)]

        for m in maps:
            new_q = []
            print(q)
            while len(q) > 0:
                # print(q)
                a, b = q.pop(-1)

                found = False
                for dest, source, length in m:
                    res = does_intersect((a, b), (source, length))
                    # print((a, b), (source, length), res)
                    if res is not None:
                        overlap, rest = res

                        for r in rest:
                            if r[1] > 0:
                                q.append(r)

                        translated = dest + overlap[0] - source

                        new_q.append((translated, overlap[1]))
                        found = True
                        break

                if not found:
                    new_q.append((a, b))

            # print(new_q)

            q = new_q

        # print(q)
        minn = min(minn, min(x[0] for x in q))

    print(minn)
