import time

if __name__ == "__main__":
    sizes = []
    file = open("../inputs/day12_input.txt", "r")
    line = ""
    # only 6 shapes
    for i in range(6):
        # read 5 lines by 5 lines
        file.readline()
        size = 0
        for _ in range(3):
            line = file.readline().strip()
            for ch in line:
                if ch == "#":
                    size += 1
        file.readline()
        sizes.append(size)
    
    total = 0
    line = file.readline().strip()
    start_time = time.time()
    while line != "":
        dimensions, pieces = line.split(":")
        width, height = dimensions.split("x")
        grid_size = int(width) * int(height)
        
        pieces = pieces.strip().split(" ")
        assert len(pieces) == len(sizes) == 6
        curr_size = 0
        for i in range(6):
            curr_size += int(pieces[i]) * sizes[i]
        
        # heuristic: curr size was approx 70% of grid size...
        if grid_size > curr_size:
            # print(grid_size, curr_size)
            # print(curr_size / grid_size)
            total += 1
        line = file.readline().strip()
    
    end_time = time.time()
    print(f"Answer for part one: {total}")
    print(f"Execution time for part one: {end_time - start_time:.6f} seconds")
