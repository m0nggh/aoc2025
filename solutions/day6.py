import time

if __name__ == "__main__":
    file = open("../inputs/day6_input.txt", "r")
    line = file.readline()
    values = []
    replaced_values = [] # for part 2
    # obtain all the values first in an array format
    values_with_spaces = line.strip().split(" ")
    replaced_string = line.replace(" ", "0") # replace with 0s first
    replaced_values.append(replaced_string) # for part 2
    # for part one
    for value in values_with_spaces:
        if value != "":
            values.append([value])

    line = file.readline()
    while not line.startswith("*" ) and not line.startswith("+"):
        # for part one
        values_with_spaces = line.strip().split(" ")
        index = 0
        for value in values_with_spaces:
            if value == "":
                continue
            values[index].append(value)
            index += 1

        # for part two
        replaced_string = line.replace(" ", "0") # replace with 0s first
        replaced_values.append(replaced_string)
        line = file.readline()
    
    # obtain the operations
    operations = []
    raw_operations = []
    while line != "":
        operations_with_spaces = line.strip().split(" ")
        for op in operations_with_spaces:
            if op == "":
                continue
            operations.append(op)
        
        # for part 2
        raw_operations = list(line + " ") # somehow the last space is missing for my algo
        line = file.readline()
    assert(len(operations) == len(values))
    
    # part 1: straightforward arithmetic
    start_time = time.time()
    total, n = 0, len(operations)
    for i in range(n):
        op, curr = operations[i], 0
        if op == "*":
            curr = 1
            for val in values[i]:
                curr *= int(val)
        else:
            for val in values[i]:
                curr += int(val)
        total += curr
    
    end_time = time.time()
    print(f"Answer for part one: {total}")
    print(f"Execution time for part one: {end_time - start_time:.6f} seconds")

    # part 2: format the values here based on operations
    start_time = time.time()
    operations_index = 1
    row_index = 0
    modified_values = [[] for _ in range(n)]
    for _ in range(n):
        values_index = operations_index - 1
        max_len = 0
        while operations_index < len(raw_operations) and raw_operations[operations_index] == " ":
            max_len += 1
            operations_index += 1
        for row in replaced_values:
            modified_values[row_index].append(row[values_index : operations_index])
        row_index += 1
        operations_index += 1        


    total = 0
    new_values = [[] for _ in range(n)]
    index = 0
    for arr in modified_values:
        # take length based on the first value since all same
        val_len = len(arr[0])
        for i in range(val_len - 1, -1, -1):
            new_val = ""
            for val in arr:
                if val[i] != "0":
                    new_val += val[i]
            if new_val != "":
                new_values[index].append(int(new_val))
        index += 1
    
    for i in range(n):
        op, curr = operations[i], 0
        if op == "*":
            curr = 1
            for val in new_values[i]:
                curr *= val
        else:
            for val in new_values[i]:
                curr += val
        total += curr
    
    end_time = time.time()
    print(f"Answer for part two: {total}")
    print(f"Execution time for part two: {end_time - start_time:.6f} seconds")
