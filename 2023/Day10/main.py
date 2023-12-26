
class Map:
    def __init__(self):
        self.matrix = None
        self.initial_position = None
        #up, right, down, left
        self.conections = {
            '|': [['S', '7', 'F', '|'], [], ['S', 'L', 'J', '|'], []],
            '-': [[], ['S', '7', 'J', '-'], [], ['S', 'F', 'L', '-']],
            'F': [[], ['S', '7', '-', 'J'], ['S', '|', 'L', 'J'], []],
            '7': [[], [], ['S', '|', 'L', 'J'], ['S', '-', 'F', 'L']],
            'L': [['S', '|', '7', 'F'], ['S', '-', 'J', '7'], [], []],
            'J': [['S', '|', 'F', '7'], [], [], ['S', '-', 'L', 'F']],
            'S': [['|', '7', 'F'], ['-', 'J'], ['|', 'L', 'J'], ['-', 'L']],
        }

    def read(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        lines = [line.strip() for line in lines if line.strip()]
        self.matrix = [list(line) for line in lines]

        # Find and store the position of 'S'
        for i, row in enumerate(self.matrix):
            for j, char in enumerate(row):
                if char == 'S':
                    self.initial_position = (i, j)
                    break
            if self.initial_position:
                break

    def connects(self, char, direction, current_char):
        if direction == "up":
            return char in self.conections[current_char][0]
        elif direction == "right":
            return char in self.conections[current_char][1]
        elif direction == "down":
            return char in self.conections[current_char][2]
        elif direction == "left":
            return char in self.conections[current_char][3]

    def find_steps(self):
        steps = 0
        found = False
        position = self.initial_position
        where_from = None
        
        while not found:
            current_char = self.matrix[position[0]][position[1]]

            # Check upper char
            if position[0] > 0 and where_from != "up":
                upper_char = self.matrix[position[0] - 1][position[1]]
                if self.connects(upper_char, "up", current_char):
                    #print("Going up")
                    #print(upper_char)
                    if upper_char == 'S':
                        found = True
                    position = (position[0] - 1, position[1])
                    where_from = "down"
                    steps += 1
                    continue
            
            # Check right char
            if position[1] < len(self.matrix[0]) - 1 and where_from != "right":
                right_char = self.matrix[position[0]][position[1] + 1]
                if self.connects(right_char, "right", current_char):
                    #print("Going right")
                    #print(right_char)
                    if right_char == 'S':
                        found = True
                    position = (position[0], position[1] + 1)
                    where_from = "left"
                    steps += 1
                    continue

            # Check down char
            if position[0] < len(self.matrix) - 1 and where_from != "down":
                down_char = self.matrix[position[0] + 1][position[1]]
                if self.connects(down_char, "down", current_char):
                    #print("Going down")
                    #print(down_char)
                    if down_char == 'S':
                        found = True
                    position = (position[0] + 1, position[1])
                    where_from = "up"
                    steps += 1
                    continue

            # Check left char
            if position[1] > 0 and where_from != "left":
                left_char = self.matrix[position[0]][position[1] - 1]
                if self.connects(left_char, "left", current_char):
                    #print("Going left")
                    #print(left_char)
                    if left_char == 'S':
                        found = True
                    position = (position[0], position[1] - 1)
                    where_from = "right"
                    steps += 1
                    continue
        
        return steps/2
    

    def flood_fill(self, x, y):
        if x < 0 or y < 0 or x >= len(self.matrix) or y >= len(self.matrix[0]):
            return
        if self.matrix[x][y] == '.':
            self.matrix[x][y] = 'O'
        else:
            # Respect pipe connections
            current_char = self.matrix[x][y]
            if current_char == 'O':
                return
            if x > 0 and self.connects(self.matrix[x - 1][y], "up", current_char) and self.matrix[x - 1][y] == '.':
                self.flood_fill(x - 1, y)
            if y < len(self.matrix[0]) - 1 and self.connects(self.matrix[x][y + 1], "right", current_char) and self.matrix[x][y + 1] == '.':
                self.flood_fill(x, y + 1)
            if x < len(self.matrix) - 1 and self.connects(self.matrix[x + 1][y], "down", current_char) and self.matrix[x + 1][y] == '.':
                self.flood_fill(x + 1, y)
            if y > 0 and self.connects(self.matrix[x][y - 1], "left", current_char) and self.matrix[x][y - 1] == '.':
                self.flood_fill(x, y - 1)

    def count_enclosed_tiles(self):
        # Start flood fill from the edges
        for x in range(len(self.matrix)):
            self.flood_fill(x, 0)
            self.flood_fill(x, len(self.matrix[0]) - 1)
        for y in range(len(self.matrix[0])):
            self.flood_fill(0, y)
            self.flood_fill(len(self.matrix) - 1, y)

        count = 0
        for row in self.matrix:
            count += row.count('.')

        return count

    def print_map(self):
        for row in self.matrix:
            print(row)
        print()

map_instance = Map()
map_instance.read('example.txt')

print(map_instance.find_steps())

enclosed_tiles = map_instance.count_enclosed_tiles()
print(map_instance.print_map())
print(f"Number of tiles enclosed by the loop: {enclosed_tiles}")