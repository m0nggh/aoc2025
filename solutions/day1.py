import time

def parse_input():
    data = []
    with open("../inputs/day1_input.txt", "r") as file:
        data = file.read().split("\n")
    data.pop()
    for i in range(len(data)):
        row = data[i]
        data[i] = (row[0], int(row[1:]))
    return data

def part_one(data) -> int:
    dial, count = 50, 0
    for dir, rotation in data:
        dial = (dial - rotation) % 100 if dir == "L" else (dial + rotation) % 100
        if dial == 0:
            count += 1
    return count

# 8 WA is crazy...
def part_two(data) -> int:
    dial, count = 50, 0
    # literally skip the math because too many edge cases...
    for dir, rotation in data:
        while rotation > 0:
            if dir == "L":
                if dial == 0:
                    dial = 100
                diff = dial
                if rotation >= diff:
                    count += 1
                    dial = 0
                else:
                    dial -= rotation
                rotation -= diff
            else:
                if dial == 100:
                    dial = 0
                diff = 100 - dial
                if rotation >= diff:
                    count += 1
                    dial = 100
                else:
                    dial += rotation
                rotation -= diff
    return count

if __name__ == "__main__":
    data = parse_input()
    print(part_one(data))
    print(part_two(data))