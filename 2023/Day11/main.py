import math

expansion_factor = 1000000

def expand_universe(matrix):
    rows_to_duplicate = [i for i, row in enumerate(matrix) if set(row) == {'.'}]
    cols_to_duplicate = [j for j in range(len(matrix[0])) if all(matrix[i][j] == '.' for i in range(len(matrix)))]

    return rows_to_duplicate, cols_to_duplicate



def get_galaxies_positions(universe):
    return [(i, j) for i, row in enumerate(universe) for j, cell in enumerate(row) if cell == '#']

def dist_between_galaxies(galaxy1, galaxy2, expansion_rows, expansion_cols):
    # Check how many values in between are in expansion_indices_rows and expansion_indices_cols
    lower_bound_row = min(galaxy1[0], galaxy2[0])
    upper_bound_row = max(galaxy1[0], galaxy2[0])
    expansions_row = sum(lower_bound_row <= elem <= upper_bound_row for elem in expansion_rows)
    lower_bound_col = min(galaxy1[1], galaxy2[1])
    upper_bound_col = max(galaxy1[1], galaxy2[1])
    expansions_col = sum(lower_bound_col <= elem <= upper_bound_col for elem in expansion_cols) 

    return abs(galaxy2[0] - galaxy1[0]) - expansions_row + expansions_row * expansion_factor + abs(galaxy2[1] - galaxy1[1]) - expansions_col + expansions_col * expansion_factor




# Read file
with open('input.txt', 'r') as f:
    lines = [list(line.strip()) for line in f if line.strip()]


# Expand the universe
universe = lines
expansion_indices_rows, expansion_indices_cols = expand_universe(universe)


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
    distance_sum += dist_between_galaxies(pair[0], pair[1], expansion_indices_rows, expansion_indices_cols)

print(distance_sum)
