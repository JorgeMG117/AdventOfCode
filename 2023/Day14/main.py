
ROUNDED_ROCK = 'O'
CUBE_ROCK = '#'
EMPTY = '.'

def read_input(file):
    with open(file, 'r') as f:
        return f.read().split()

total_load = 0

platform = read_input("example.txt")
#print(platform)

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

            total_load += len(platform) - row_value
        elif val == EMPTY:
            empty_spaces.append(row)
        else:#CUBE_ROCK
            empty_spaces = []


print("Total load: " + str(total_load))