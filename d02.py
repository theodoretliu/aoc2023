with open("d02.txt", "r") as f:
    s = 0

    second = 0
    for i, l in enumerate(f):
        id_no = i + 1
        _, draws = l.split(":")
        draws = draws.strip()

        bags = draws.split(";")

        max_for_col = {"red": -1, "blue": -1, "green": -1}
        good = True
        for bag in bags:
            bag = bag.strip()

            marbles = bag.split(",")

            for marble in marbles:
                marble = marble.strip()

                count, color = marble.split(" ")

                count = int(count)

                if color == "red" and count > 12:
                    good = False

                if color == "green" and count > 13:
                    good = False

                if color == "blue" and count > 14:
                    good = False

                max_for_col[color] = max(count, max_for_col[color])

        prod = 1

        for x in max_for_col.values():
            prod *= x

        second += prod

        if good:
            s += id_no

    print(s)
    print(second)
