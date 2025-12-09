import time

def parse_input():
    data = []
    with open("../inputs/day3_input.txt", "r") as file:
        for row in file:
            data.append(row.strip())
    return data

def form_increasing_stack(row: str, is_reversed: bool) -> int:
    stack = []
    for ch in row:
        if not stack or ch >= stack[-1]:
            stack.append(ch)
    ans = 0
    if len(stack) < 2:
        return ans
    last_two = (stack[-1], stack[-2]) if is_reversed else (stack[-2], stack[-1])
    return int(last_two[0]) * 10 + int(last_two[1])
    

def part_one(data) -> int:
    start_time = time.time()
    total = 0
    for row in data:
        # lets just do double increasing stack and compare the max numbers
        first, second = form_increasing_stack(row, False), form_increasing_stack(row[::-1], True)
        total += max(first, second)
    end_time = time.time()
    print(f"Execution Time: {end_time - start_time:.6f} seconds")
    return total

# try brute force recursion hmm thats 12s for the test input lmaooo
def part_two(data) -> int:
    FINAL_LENGTH = 12
    start_time = time.time()
    total = 0

    def helper(row: str, index: int, output: str) -> None:
        nonlocal max_num
        if len(output) == FINAL_LENGTH:
            max_num = max(max_num, int(output))
            return

        for i in range(index, len(row)):
            helper(row, i + 1, output + row[i])
            helper(row, i + 1, output)
    
    for row in data:
        max_num = 0
        helper(row, 0, "")
        total += max_num
    
    end_time = time.time()
    print(f"Execution Time: {end_time - start_time:.6f} seconds")
    return total

# DP won't work, just greedy and always make sure you have enough digits left to "collect"
def smarter_method(data) -> None:
    # convert to an array of numbers first
    for i in range(len(data)):
        data[i] = [int(ch) for ch in data[i]]
    
    # part 1: just get first num and second num
    start_time = time.time()
    total = 0
    for row in data:
        tens_value = max(row[:-1]) # only can take up to the 2nd last item
        tens_index = row.index(tens_value) # returns first possible index for that value
        ones_value = max(row[tens_index + 1 :])
        max_value = tens_value * 10 + ones_value
        total += max_value
    end_time = time.time()
    print(f"Answer for part one: {total}")
    print(f"Execution Time: {end_time - start_time:.6f} seconds")

    # part 2: repeat but for 12 numbers (leave space accordingly)
    start_time = time.time()
    total = 0
    for row in data:
        curr = 0
        for digit in range(11, -1, -1):
            value = max(row[ : len(row) - digit])
            index = row.index(value)
            row = row[index + 1 : ] # shrink the row
            curr += 10**digit * value
        total += curr
    end_time = time.time()
    print(f"Answer for part two: {total}")
    print(f"Execution Time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    data = parse_input()
    print(part_one(data))
    # print(part_two(data))
    smarter_method(data)
