import itertools

f = open('input.txt', 'rt')


def compute(f):
    locations = set()
    distance = {}

    for line in f:
        start = line.split(" ")[0]
        end = line.split(" ")[2]

        locations.add(start)
        locations.add(end)

        distance_between = int(line.split(" ")[4])
        distance[(start, end)] = distance_between
        distance[(end, start)] = distance_between

    return locations, distance


(locations, distance) = compute(f)

path_lengths = {}

for path in itertools.permutations(locations):
    segments = [(path[i], path[i + 1]) for i in range(0, len(locations) - 1)]
    lengths = [distance[segment] for segment in segments]

    path_lengths[path] = sum(lengths)


out = open("output2.txt", "w")
out.write(str(max(path_lengths.values())))
out.close()