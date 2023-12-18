# Return list of patterns 
def parse_input(file_name):
    with open(file_name, 'r') as f:
        maps = f.read().split('\n\n')
    return [map.split('\n') for map in maps]

"""
123456789
    ><   
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
    ><   
123456789

return 5 columns to its left
"""
def vertical_reflection(pattern):
    # Loop through each column
    for i in range(1, len(pattern[0])):

        out = False
        idx_1 = i
        idx_2 = i - 1
        simetric = 0
        while not out:
            if idx_2 < 0 or idx_1 >= len(pattern[0]) or simetric > 1:
                out = True
                break

            for j in range(0, len(pattern)):
                # Check if vertical reflection
                if pattern[j][idx_1] != pattern[j][idx_2]:
                    simetric = simetric + 1
            
            idx_1 += 1
            idx_2 -= 1
        
        if simetric == 1:#The one that is 
            return i
    return 0

"""
1 #...##..# 1
2 #....#..# 2
3 ..##..### 3
4v#####.##.v4
5^#####.##.^5
6 ..##..### 6
7 #....#..# 7

return 4 rows above it
"""
def horizontal_reflection(pattern):
    # Loop through each row
    for i in range(1, len(pattern)):
        out = False
        idx_1 = i
        idx_2 = i - 1
        simetric = 0
        while not out:
            if idx_2 < 0 or idx_1 >= len(pattern) or simetric > 1:
                out = True
                break

            for j in range(0, len(pattern[0])):
                # Check if horizontal reflection
                if pattern[idx_1][j] != pattern[idx_2][j]:
                    simetric = simetric + 1
            
           
            idx_1 += 1
            idx_2 -= 1

        if simetric == 1:
            return i

    return 0

ASH = '.'
ROCKS = '#'

summarize = 0

data = parse_input('input.txt')

for pattern in data:
    print("Pattern: ")
    for line in pattern:
        print(line)
    print()

    # Find vertical line of reflection
    num_cols = 0
    num_cols = vertical_reflection(pattern)
    print("Num cols: ", num_cols)

    if num_cols > 0:
        summarize += num_cols
        continue

    # Find horizontal line of reflection
    num_rows = horizontal_reflection(pattern)
    print("Num rows: ", num_rows)
    summarize += 100*num_rows

print("Summarize: ", summarize)


