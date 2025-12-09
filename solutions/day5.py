import time


if __name__ == "__main__":
    count = 0
    file = open("../inputs/day5_input.txt", "r")
    line = file.readline().strip()
    # obtain the ranges first
    ranges = []
    while line != "":
        start, end = line.split("-")
        ranges.append([int(start), int(end)])
        line = file.readline().strip()
    
    # check every ingredient with every range
    start_time = time.time()
    total = 0
    line = file.readline().strip()
    while line != "":
        val = int(line)
        for start, end in ranges:
            if val >= start and val <= end:
                total += 1
                break
        line = file.readline().strip()
    end_time = time.time()
    print(f"Answer for part one: {total}")
    print(f"Execution time for part one: {end_time - start_time:.6f} seconds")

    # part two crux: how to determine duplicates in ranges
    # seems like overlapping ranges would work here, sort by start time,
    # then just merge intervals, and in the end calculate the total
    start_time = time.time()
    ranges.sort()
    i, n = 0, len(ranges)
    merged_ranges = []
    while i < n:
        curr = ranges[i]
        i += 1
        while i < n and ranges[i][0] <= curr[1]:
            curr[1] = max(curr[1], ranges[i][1]) # combine and extend end range
            i += 1
        merged_ranges.append(curr.copy())
    total = 0
    print(merged_ranges)
    for start, end in merged_ranges:
        total += end - start + 1
    end_time = time.time()
    print(f"Answer for part two: {total}")
    print(f"Execution time for part two: {end_time - start_time:.6f} seconds")
