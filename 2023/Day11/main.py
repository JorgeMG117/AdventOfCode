import math

def expand_universe(matrix):
    rows_to_duplicate = [i for i, row in enumerate(matrix) if set(row) == {'.'}]
    cols_to_duplicate = [j for j in range(len(matrix[0])) if all(matrix[i][j] == '.' for i in range(len(matrix)))]

    for i in sorted(rows_to_duplicate, reverse=True):
        matrix.insert(i, matrix[i])

    transposed_matrix = list(map(list, zip(*matrix)))

    for j in sorted(cols_to_duplicate, reverse=True):
        transposed_matrix.insert(j, transposed_matrix[j])

    return list(map(list, zip(*transposed_matrix)))


def get_galaxies_positions(universe):
    return [(i, j) for i, row in enumerate(universe) for j, cell in enumerate(row) if cell == '#']

def dist_between_galaxies(galaxy1, galaxy2):
    return abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1])




# Read file
with open('input.txt', 'r') as f:
    lines = [list(line.strip()) for line in f if line.strip()]


# Expand the universe
universe = expand_universe(lines)
# print(universe)

# Get galaxies positions and create pairs of galaxies
galaxies_pairs = []
galaxies_positions = get_galaxies_positions(universe)
for i in range(len(galaxies_positions)):
    for j in range(i + 1, len(galaxies_positions)):
        galaxies_pairs.append((galaxies_positions[i], galaxies_positions[j]))

# print(len(galaxies_pairs))


# Compute the distance between each pair of galaxies
distance_sum = 0
for pair in galaxies_pairs:
    # print("Pair: ", pair)
    # print("Distance: ", dist_between_galaxies(pair[0], pair[1]))
    # print()
    distance_sum += dist_between_galaxies(pair[0], pair[1])

print(distance_sum)
