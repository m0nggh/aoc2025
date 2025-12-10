import time, bisect

if __name__ == "__main__":
    points = []
    file = open("../inputs/day9_input.txt", "r")
    for line in file:
        x, y = line.strip().split(",")
        points.append((int(x), int(y)))
    
    n = len(points)
    max_area = 0
    # part 1: brute force and check all points
    start_time = time.time()
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            curr_area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            max_area = max(max_area, curr_area)
    
    end_time = time.time()
    print(f"Answer for part one: {max_area}")
    print(f"Execution time for part one: {end_time - start_time:.6f} seconds")

    '''
    part 2: how to tell that your rectangle have only green tiles inside
    1. all four corners must be within the big polygon
    2. use ray casting algo to determine: every point must cross only
    odd number of times while moving rightwards towards infinity
    difficult because need to include coordinate compression also, so skipz this method
    '''
    start_time = time.time()
    max_area = -1
    
    '''
    Ended up just getting all the rectangle sizes and sorted in descending order
    Then, get all the edges in ascending x order
    And check that every edge bounding box does not overlap the rectangle --> found answer
    '''
    def calculate_size(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    
    edges, sizes = [], []
    for i in range(n):
        edges.append(sorted((points[i], points[i - 1]))) # this works for cyclic
        for j in range(i + 1, n):
            p1, p2 = sorted((points[i], points[j])) # ensures x1 <= x2
            sizes.append((calculate_size(p1, p2), p1, p2))
        
    # largest edge tend to cause the biggest issues
    edges.sort(reverse=True, key=lambda edge : calculate_size(edge[0], edge[1]))
    sizes.sort(reverse=True)

    for size, (x1, y1), (x2, y2) in sizes:
        y1, y2 = sorted((y1, y2)) # ensures y1 <= y2 since sizes dont guarantee that
        is_inside = True
        for (x3, y3), (x4, y4) in edges:
            if x4 > x1 and x3 < x2 and y4 > y1 and y3 < y2:
                is_inside = False
                break
        if is_inside:
            max_area = size
            break
            
    end_time = time.time()
    print(f"Answer for part two: {max_area}")
    print(f"Execution time for part two: {end_time - start_time:.6f} seconds")
