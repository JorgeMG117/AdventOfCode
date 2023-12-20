
ROUNDED_ROCK = 'O'
CUBE_ROCK = '#'
EMPTY = '.'

def read_input(file):
    with open(file, 'r') as f:
        data = f.read().split()
    
    # Transform each line into a list of characters
    data = [list(line) for line in data]
    return data
    

def load_north_support_beams(platform):
    load = 0
    # Read column by column
    for col in range(len(platform[0])):
        empty_spaces = []
        for row in range(len(platform)):
            val = platform[row][col]

            if val == ROUNDED_ROCK:
                row_value = row
                if len(empty_spaces) > 0:
                    row_value = empty_spaces.pop(0)
                    empty_spaces.append(row)

                load += len(platform) - row_value
            elif val == EMPTY:
                empty_spaces.append(row)
            else:#CUBE_ROCK
                empty_spaces = []
    return load


def tilt(platform, direction):
    if direction == 'N':
        for col in range(len(platform[0])):
            empty_spaces = []
            for row in range(len(platform)):
                val = platform[row][col]

                if val == ROUNDED_ROCK:
                    row_value = row
                    if len(empty_spaces) > 0:
                        row_value = empty_spaces.pop(0)
                        empty_spaces.append(row)
                        platform[row][col] = '.'

                    platform[row_value][col] = 'O'
                elif val == EMPTY:
                    empty_spaces.append(row)
                else:#CUBE_ROCK
                    empty_spaces = []
    elif direction == 'W':
        for row in range(len(platform)):
            empty_spaces = []
            for col in range(len(platform[0])):
                val = platform[row][col]

                if val == ROUNDED_ROCK:
                    col_value = col
                    if len(empty_spaces) > 0:
                        col_value = empty_spaces.pop(0)
                        empty_spaces.append(col)
                        platform[row][col] = '.'

                    platform[row][col_value] = 'O'
                elif val == EMPTY:
                    empty_spaces.append(col)
                else:#CUBE_ROCK
                    empty_spaces = []

    elif direction == 'S':
        for col in range(len(platform[0])):
            empty_spaces = []
            for row in range(len(platform)-1, -1, -1):
                val = platform[row][col]

                if val == ROUNDED_ROCK:
                    row_value = row
                    if len(empty_spaces) > 0:
                        row_value = empty_spaces.pop(0)
                        empty_spaces.append(row)
                        platform[row][col] = '.'

                    platform[row_value][col] = 'O'
                elif val == EMPTY:
                    empty_spaces.append(row)
                else:#CUBE_ROCK
                    empty_spaces = []
    elif direction == 'E':
        for row in range(len(platform)):
            empty_spaces = []
            for col in range(len(platform[0])-1, -1, -1):
                val = platform[row][col]

                if val == ROUNDED_ROCK:
                    col_value = col
                    if len(empty_spaces) > 0:
                        col_value = empty_spaces.pop(0)
                        empty_spaces.append(col)
                        platform[row][col] = '.'

                    platform[row][col_value] = 'O'
                elif val == EMPTY:
                    empty_spaces.append(col)
                else:#CUBE_ROCK
                    empty_spaces = []

    return platform

total_load = 0

platform = read_input("example.txt")
# print(len(platform))
# print(len(platform[0]))

# north, then west, then south, then east
cycles = 1000000000
#cycles = 4

directions = ['N', 'W', 'S', 'E']
for cycle in range(cycles):
    for direction in directions:
            platform = tilt(platform, direction)


total_load = load_north_support_beams(platform)


print("Total load: " + str(total_load))