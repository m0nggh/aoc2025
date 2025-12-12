import time
from functools import cache

if __name__ == "__main__":
    graph = {}
    file = open("../inputs/day11_input.txt", "r")
    for line in file:
        source, dests = line.strip().split(":")
        if source not in graph:
            graph[source] = []
        for dest in dests.strip().split(" "):
            graph[source].append(dest)
    
    # part 1: perform dfs
    start_time = time.time()
    SRC_NODE = "you"

    # DAG: No cycles so no need for visited set
    @cache
    def dfs(node: str, dest_node: str) -> int:
        if node == dest_node:
            return 1

        # only applicable for "out" here but sanity check
        if node not in graph:
            return 0
        
        ways = 0
        for neigh in graph[node]:
            ways += dfs(neigh, dest_node)
        return ways
    
    count = dfs(SRC_NODE, "out")
    end_time = time.time()
    print(f"Answer for part one: {count}")
    print(f"Execution time for part one: {end_time - start_time:.6f} seconds")

    '''
    part 2: perform dfs for these 2 paths
        1. src --> dac --> fft --> out
        2. src --> fft --> dac --> out
    for each path, take the product of all 3 subpaths then sum both
    '''
    first_path_count = dfs("svr", "dac") * dfs("dac", "fft") * dfs("fft", "out")
    print(f"Count from svr --> dac --> fft --> out: {first_path_count}")
    second_path_count = dfs("svr", "fft") * dfs("fft", "dac") * dfs("dac", "out")
    print(f"Count from svr --> fft --> dac --> out: {second_path_count}")

    count = first_path_count + second_path_count
    end_time = time.time()
    print(f"Answer for part two: {count}")
    print(f"Execution time for part two: {end_time - start_time:.6f} seconds")
