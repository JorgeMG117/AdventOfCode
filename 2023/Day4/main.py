

points = 0

# Read file
with open("input.txt", "r") as file:
    data = file.read().splitlines()

#print(data)
for card in data:
    card_points = 0

    # Split string by char | into two parts
    card = card.split("|")

    # Process each part and convert to lists of ints
    winnning_numbers = [int(num) for num in card[0].split()[2:]]
    my_numbers = [int(num) for num in card[1].split()]

    # Transform winning_numbers to map
    winning_numbers = {num: True for num in winnning_numbers}

    # Check if my numbers are in winning numbers
    for num in my_numbers:
        if num in winning_numbers:
            if card_points == 0:
                card_points = 1
            else:
                card_points = card_points * 2

    points += card_points

    
print(points)




