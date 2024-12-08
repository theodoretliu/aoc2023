with open("d05.txt", "r") as f:
    seeds = f.readline()
    _, seeds = seeds.strip().split(":")
    seeds = [int(seed) for seed in seeds.split()]

    f.readline()

    maps = []

    for _ in range(7):
        f.readline()  # name of the map
        current_map = []

        while len((line := f.readline().strip())) > 0:
            start1, start2, length = line.strip().split()
            current_map.append((int(start1), int(start2), int(length)))

        maps.append(current_map)

    minn = float("inf")

    for seed in seeds:
        next_one = seed
        for m in maps:
            found = False
            for dest, source, length in m:
                if source <= next_one < source + length:
                    next_one = dest + next_one - source
                    found = True
                    break

        minn = min(minn, next_one)

    print(minn)
