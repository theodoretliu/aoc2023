times = [56, 97, 78, 75]
distances = [546, 1927, 1131, 1139]

p = 1
for time, distance in zip(times, distances):
    count = 0
    for i in range(time):
        if i * (time - i) > distance:
            count += 1

    p *= count

time = 56977875
distance = 546192711311139
# solve with wolfram alpha and do right - left + 1


print(p)
