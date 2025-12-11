import time
from collections import deque
import pulp as pl

if __name__ == "__main__":
    lights_data, buttons_data, joltage_data = [], [], []
    file = open("../inputs/day10_input.txt", "r")
    for line in file:
        lights, rest = line.strip().split("]")
        lights_data.append(tuple(lights[1:])) # (".", "#", "#", ".")
        buttons_row, joltage_row = rest.split("{")
        
        # parsing the buttons row... (3), (1,2,3), (2,3) ...
        buttons = buttons_row.strip().split("(")
        buttons_row = [] # [[3], [1,2,3], [2,3]]
        for button in buttons:
            if button == "":
                continue
            digits = button.split(",")
            digits_arr = []
            for digit in digits:
                digit = digit.split(")")[0]
                if digit == "":
                    continue
                digits_arr.append(int(digit))
            buttons_row.append(digits_arr)
        buttons_data.append(buttons_row)

        joltage = joltage_row[:-1]
        joltage_data.append([int(val) for val in joltage.split(",")]) # [3,5,4,7]

    n = len(lights_data)
    assert len(lights_data) == len(buttons_data) == len(joltage_data)

    # part 1: use bfs to get shortest path and terminate early
    start_time = time.time()
    total_presses = 0

    def is_pattern_matching(arr1: tuple[str], arr2: tuple[str]) -> bool:
        assert len(arr1) == len(arr2)
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        return True

    def generate_next_pattern(arr: tuple[str], button: list[int]) -> tuple:
        new_arr = list(arr)
        for digit in button:
            new_arr[digit] = "." if new_arr[digit] == "#" else "#"
        return tuple(new_arr)

    for i in range(n):
        lights, buttons = lights_data[i], buttons_data[i]
        # print(f"iteration {i}")
        # print(lights)
        # print(buttons)
        curr_pattern = tuple(["."] * len(lights))
        queue = deque([curr_pattern])
        visited = set()
        presses = min_presses = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                curr_pattern = queue.popleft()
                if is_pattern_matching(lights, curr_pattern):
                    min_presses = presses
                    break

                if curr_pattern in visited:
                    continue
                visited.add(curr_pattern)
                
                for button in buttons:
                    next_pattern = generate_next_pattern(curr_pattern, button)
                    if next_pattern in visited:
                        continue
                    queue.append(next_pattern)
            
            presses += 1
            if min_presses != 0:
                break
        
        # print(f"Min presses: {min_presses}")
        total_presses += min_presses
        
    end_time = time.time()
    print(f"Answer for part one: {total_presses}")
    print(f"Execution time for part one: {end_time - start_time:.6f} seconds")

    '''
    part 2: still use bfs to get shortest path and terminate early
    but joltage too big, note voltage can only go up and not down
    so stop using buttons that increase that voltage when the limit is reached

    jk: raise white flag, have to seek help for linear algerba
    '''
    start_time = time.time()
    total_presses = 0

    '''
    Turning puzzle into an integer linear programming problem
    Example for first test input:
    Buttons:
        0: (3)
        1: (1,3)
        2: (2)
        3: (2,3)
        4: (0,2)
        5: (0,1)

    Target: {3,5,4,7} → counters 0..3

    Let variables be:
        x0 = presses of (3)
        x1 = presses of (1,3)
        x2 = presses of (2)
        x3 = presses of (2,3)
        x4 = presses of (0,2)
        x5 = presses of (0,1)
    
    Counter 0 is touched by buttons 4 and 5: x4 + x5 == 3
    Counter 1 is touched by buttons 1 and 5: x1 + x5 == 5
    Counter 2 is touched by buttons 2, 3, 4: x2 + x3 + x4 == 4
    Counter 3 is touched by buttons 0, 1, 3: x0 + x1 + x3 == 7
    Objective: x0 + x1 + x2 + x3 + x4 + x5  (minimise this)
    '''
    def solve_machine(buttons, target):
        k = len(buttons)
        var_names = [f"x{i}" for i in range(k)]
        prob = pl.LpProblem("buttons", pl.LpMinimize)
        vars_ = {v: pl.LpVariable(v, lowBound=0, cat="Integer") for v in var_names}

        prob += pl.lpSum(vars_.values()) # objective

        # Constraints per counter
        m = len(target)
        A = [[0] * k for _ in range(m)] # coefficient matrix A of size m x k
        # A[j][b] = 1 if button b affects counter j
        # A[j][b] = 0 otherwise
        for b_idx, indices in enumerate(buttons):
            for j in indices:
                A[j][b_idx] = 1

        for j in range(m):
            prob += (
                pl.lpSum(A[j][b] * vars_[f"x{b}"] for b in range(k)) == target[j]
            )

        prob.solve(pl.PULP_CBC_CMD(msg=False))
        # for v in var_names:
        #     print(pl.value(vars_[v]))
        total_presses = sum(pl.value(vars_[v]) for v in var_names)
        return int(total_presses)

    for i in range(n):
        buttons, joltage = buttons_data[i], joltage_data[i]
        presses = solve_machine(buttons, joltage)
        # print(f"Presses: {presses}")
        total_presses += presses
        
    end_time = time.time()
    print(f"Answer for part two: {total_presses}")
    print(f"Execution time for part two: {end_time - start_time:.6f} seconds")
                
                
                

        

        
