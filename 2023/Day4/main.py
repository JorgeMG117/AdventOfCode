points = 0

# Read file
with open("input.txt", "r") as file:
    data = file.read().splitlines()

# Create empyt int list
copies = []

#print(data)
for i, card in enumerate(data):
    # Add original coppy
    if i >= len(copies):
        copies.append(1)
    else:
        copies[i] += 1

    # Split string by char | into two parts
    card = card.split("|")

    # Process each part and convert to lists of ints
    winnning_numbers = [int(num) for num in card[0].split()[2:]]
    my_numbers = [int(num) for num in card[1].split()]

    # Transform winning_numbers to map
    winning_numbers = {num: True for num in winnning_numbers}

    # Check if my numbers are in winning numbers
    k = i + 1
    for num in my_numbers:
        if num in winning_numbers:
            if k < len(copies):
                copies[k] += copies[i]
            else:
                copies.append(copies[i])
            k += 1

    points += copies[i]

    
print(points)




