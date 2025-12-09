import time
from collections import deque
from functools import cache

if __name__ == "__main__":
    matrix = []
    file = open("../inputs/day7_input.txt", "r")
    for line in file:
        matrix.append(list(line.strip()))
    
    ROWS, COLS = len(matrix), len(matrix[0])
    # part one
    queue = deque()
    visited = set()
    start_node = (0, 0)
    # find the start node first
    for c in range(COLS):
        if matrix[0][c] == "S":
            queue.append((1, c))
            start_node = (1, c)
            break
    
    start_time = time.time()
    total = 0
    while queue:
        # if ., insert one below, if ^, insert left and right
        r,c = queue.popleft()
        if r == ROWS - 1:
            continue
        if c == -1 or c == COLS:
            continue
        if (r,c) in visited:
            continue

        visited.add((r, c))
        val = matrix[r][c]
        if val == ".":
            queue.append((r + 1, c))
        elif val == "^":
            total += 1
            queue.append((r, c + 1))
            queue.append((r, c - 1))
    
    end_time = time.time()
    print(f"Answer for part one: {total}")
    print(f"Execution time for part one: {end_time - start_time:.6f} seconds")


    # part 2: attempt dfs, cant tell the time complexity
    start_time = time.time()
    visited = set()
    dp = {}
    @cache
    def dfs(r: int, c: int) -> int:
        if r >= ROWS or r < 0 or c >= COLS or c < 0 or (r, c) in visited:
            return 0

        if r == ROWS - 1:
            return 1

        # if (r, c) in dp:
        #     return dp[(r, c)]

        ways = 0
        val = matrix[r][c]
        visited.add((r, c))
        if val == ".":
            ways += dfs(r + 1, c)
        elif val == "^":
            ways += dfs(r, c + 1)
            ways += dfs(r, c - 1)
    
        visited.remove((r, c))
        # dp[(r, c)] = ways
        return ways
    
    total = dfs(start_node[0], start_node[1])
    end_time = time.time()
    print(f"Answer for part two: {total}")
    print(f"Execution time for part two: {end_time - start_time:.6f} seconds")
