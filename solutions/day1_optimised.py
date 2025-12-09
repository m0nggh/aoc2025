import time

# adopted from an online solution
def main():
    start_time = time.time()

    dial = 50
    part1, part2 = 0, 0

    with open("input.txt", "rt") as fin:

        for line in fin:
            dial_before = dial

            if line[0] == "R":
                dial = dial_before + int(line[1:])
                part2 += dial // 100 - dial_before // 100
            else:
                dial = dial_before - int(line[1:])
                part2 += (dial_before - 1) // 100 - (dial - 1) // 100

            if dial % 100 == 0:
                part1 += 1

    end_time = time.time()

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
    print(f"Execution Time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()