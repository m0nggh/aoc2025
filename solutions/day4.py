import time
from collections import deque

ROWS = COLS = 0
dirs = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

def parse_input():
    matrix = []
    with open("../inputs/day4_input.txt", "r") as file:
        for row in file:
            matrix.append(list(row.strip()))
    return matrix

def part_one(matrix) -> int:
    start_time = time.time()
    total = 0
    for r in range(ROWS):
        for c in range(COLS):
            count = 0
            if matrix[r][c] == ".":
                continue

            for y,x in dirs:
                r1, c1 = r + y, c + x
                if r1 < 0 or r1 >= ROWS or c1 < 0 or c1 >= COLS or matrix[r1][c1] == ".":
                    continue
                count += 1
            if count < 4:
                total += 1
    end_time = time.time()
    print(f"Answer for part one: {total}")
    print(f"Execution Time for part one: {end_time - start_time:.6f} seconds")
    return total

def part_two(matrix) -> int:
    # bfs, just keep adding more rolls to check, but we need to keep track
    # of the count of the neighbours to avoid unnecessary adding
    start_time = time.time()
    total = 0
    queue, m, checked = deque(), {}, set()
    for r in range(ROWS):
        for c in range(COLS):
            count = 0
            if matrix[r][c] == ".":
                continue

            for y,x in dirs:
                r1, c1 = r + y, c + x
                if r1 < 0 or r1 >= ROWS or c1 < 0 or c1 >= COLS or matrix[r1][c1] == ".":
                    continue
                count += 1
            
            if count < 4:
                queue.append((r,c))
            m[(r,c)] = count
    
    # bfs from here
    while queue:
        size = len(queue)
        layer_count = 0 # to determine whether to exit early
        for _ in range(size):
            r,c = queue.popleft()
            if matrix[r][c] == ".":
                continue

            count = 0
            curr_neighbours = []
            for y,x in dirs:
                r1, c1 = r + y, c + x
                if r1 < 0 or r1 >= ROWS or c1 < 0 or c1 >= COLS or matrix[r1][c1] == ".":
                    continue
                count += 1
                curr_neighbours.append((r1,c1))
            
            if (r,c) not in checked and count < 4:
                matrix[r][c] = "." # directly mutate the matrix once checked
                total += 1
                layer_count += 1
                checked.add((r,c))

                for r1, c1 in curr_neighbours:
                    m[(r1,c1)] -= 1 # update and see whether to add to queue
                    if m[((r1,c1))] < 4:
                        queue.append((r1, c1))
        if layer_count == 0:
            break
        print(total)

    end_time = time.time()
    print(f"Answer for part two: {total}")
    print(f"Execution Time for part two: {end_time - start_time:.6f} seconds")
    return total

if __name__ == "__main__":
    matrix = parse_input()
    ROWS, COLS = len(matrix), len(matrix[0])
    part_one(matrix)
    part_two(matrix)