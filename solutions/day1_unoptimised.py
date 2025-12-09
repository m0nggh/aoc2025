start = 50
part_1 = 0
part_2 = 0
text_file = "1_1_input.txt"

# adopted super brute force solution online
with open(text_file) as f:
    lines = f.readlines()

for line in lines:
    direction = line[0]
    value = int(line[1:])

    while value > 0:
        start = start + (1 if direction == "R" else -1)
        value -= 1

        if start < 0:
            start = 99
        elif start > 99:
            start = 0

        if start == 0:
            part_2 += 1

    if start == 0:
        part_1 += 1

print(part_1, part_2)