import time

def parse_input():
    data = []
    line = ""
    with open("../inputs/day2_input.txt", "r") as file:
        line = file.readline()
    values = line.split(",")
    for value in values:
        start, end = value.split("-")
        data.append((start, end))
    return data

def is_double(s: str) -> bool:
    n = len(s)
    if n % 2 != 0:
        return False
    for i in range(n // 2):
        if s[i] != s[i + n // 2]:
            return False
    return True

def is_repeat(s: str) -> bool:
    interval, n = 1, len(s)
    while interval < n:
        if n % interval != 0:
            interval += 1
            continue
        
        i, is_valid = 0, True
        while i < interval:
            j, curr = i, s[i]
            while j < n:
                if s[j] != curr:
                    is_valid = False
                    break
                j += interval
            
            if not is_valid:
                break # early termination once the repeat is not found
            i += 1
        
        if is_valid:
            return True # early termination upon first repeat
        interval += 1 # keep trying every possible interval
    return False
            
def part_one(data) -> int:
    total = 0
    for start, end in data:
        start, end = int(start), int(end)
        while start <= end:
            start_str = str(start)
            if is_double(start_str):
                total += start
            start += 1
    return total

def part_two(data) -> int:
    total = 0
    for start, end in data:
        start, end = int(start), int(end)
        while start <= end:
            start_str = str(start)
            if is_repeat(start_str):
                total += start
            start += 1
    return total


if __name__ == "__main__":
    data = parse_input()
    print(part_one(data))
    start_time = time.time()
    print(part_two(data))
    end_time = time.time()
    print(f"Execution Time: {end_time - start_time:.6f} seconds")
