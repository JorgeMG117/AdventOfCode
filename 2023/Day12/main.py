
UNKNOWN = '?'
OPERATIONAL = '.'
DAMAGED = '#'

"""
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""


def process_file_content(file_path):
    # Read the file content
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Process each line to extract the pattern and the numbers
    pattern_list = []
    numbers_list = []
    for line in lines:
        pattern, numbers = line.strip().split()
        # Convert the numbers string into a list of integers
        pattern_list.append(pattern)
        numbers_list.append([int(num) for num in numbers.split(',')])

    return pattern_list, numbers_list



def arrangements(pattern, index_pattern, numbers, index_numbers):
    #print("Index pattern: ", index_pattern)
    if index_pattern == len(pattern):
        # Loop numbers
        for num in numbers:
            if num != 0:
                return 0
        #print("Returning 1")
        return 1
    elif index_numbers == len(numbers):#All numbers are used
        if pattern[index_pattern] == DAMAGED:
            return 0
        else:
            return arrangements(pattern, index_pattern + 1,
                            numbers, index_numbers)

    elif pattern[index_pattern] == OPERATIONAL:
        if numbers[index_numbers] == 0:
            #print("OPERATIONAL 0")
            return arrangements(pattern, index_pattern + 1,
                            numbers, index_numbers + 1)
        elif numbers[index_numbers] < 0:
            #print("OPERATIONAL < 0")
            return 0
        else:
            #print("OPERATIONAL > 0")
            return arrangements(pattern, index_pattern + 1,
                            numbers, index_numbers)
    elif pattern[index_pattern] == DAMAGED:
        #print("DAMAGED")
        numbers[index_numbers] -= 1
        return arrangements(pattern, index_pattern + 1,
                    numbers, index_numbers)
    elif pattern[index_pattern] == UNKNOWN:
        val1 = 0
        val2 = 0
        # Copy numbers to a new list
        numbers_copy_1 = numbers.copy()
        numbers_copy_2 = numbers.copy()
        #print("UNKNOWN")
        # Behave as OPERATIONAL
        if numbers_copy_1[index_numbers] == 0:
            #print("OPERATIONAL 0")
            val1 = arrangements(pattern, index_pattern + 1,
                            numbers_copy_1, index_numbers + 1)
        elif numbers_copy_1[index_numbers] < 0:
            #print("OPERATIONAL < 0")
            val1 = 0
        else:
            #print("OPERATIONAL > 0")
            val1 = arrangements(pattern, index_pattern + 1,
                            numbers_copy_1, index_numbers)

        # Behave as DAMAGED
        #print("DAMAGED")
        numbers_copy_2[index_numbers] -= 1
        val2 = arrangements(pattern, index_pattern + 1,
                    numbers_copy_2, index_numbers)

        print("Val1: ", val1)
        print("Val2: ", val2)
        print("Index pattern: ", index_pattern)

        return val1 + val2

# Pattern:  ?###????????
# Numbers:  [3, 2, 1]

possible_arrangements = 0

file_path = 'example.txt'
patterns, numbers = process_file_content(file_path)

for i in range(len(patterns)):
    print('Pattern: ', patterns[i])
    print('Numbers: ', numbers[i])
    res = arrangements(patterns[i], 0, numbers[i], 0)
    print('Result: ', res)

    possible_arrangements += res

print('Possible arrangements: ', possible_arrangements)

