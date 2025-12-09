import time, heapq
from math import prod, sqrt, dist

class UF:
    def __init__(self, data):
        self.m = {} # point, index
        self.index = 0
        for x,y,z in data:
            self.m[(x,y,z)] = self.index
            self.index += 1
        self.parents = [i for i in range(self.index)]
        self.ranks = [1 for _ in range(self.index)]
        self.count = self.index
    
    def find(self, index):
        if self.parents[index] != index:
            self.parents[index] = self.find(self.parents[index])
        return self.parents[index]
    
    def union(self, c1, c2):
        i1, i2 = self.m[c1], self.m[c2]
        p1, p2 = self.find(i1), self.find(i2)
        if p1 == p2:
            return
        
        if self.ranks[p1] > self.ranks[p2]:
            self.parents[p2] = p1
            self.ranks[p1] += self.ranks[p2]
        else:
            self.parents[p1] = p2
            self.ranks[p2] += self.ranks[p1]
        self.count -= 1
    
    def get_top3(self):
        ranks_with_index = [(self.ranks[i], i) for i in range(self.index)]
        ranks_with_index.sort(reverse=True)
        # need to only get those nodes where the parent == index
        count, product = 0, 1
        for rank, index in ranks_with_index:
            if index == self.parents[index]:
                product *= rank
                count += 1
            if count == 3:
                break
        return product

'''
Intuitively used UFDS cus it should help with part 2 the quickest.
But DFS for cycle detection works as well...
Reference found online: https://github.com/euporphium/pyaoc/blob/main/aoc/2025/solutions/day08_part1.py
Cleaner solution for UFDS: https://github.com/michaeljgallagher/Advent-of-Code/blob/master/2025/08.py 
'''
if __name__ == "__main__":
    data = []
    file = open("../inputs/day8_input.txt", "r")
    for line in file:
        data.append(tuple([int(val) for val in line.strip().split(",")]))
    
    start_time = time.time()
    heap, n = [], len(data)
    # throw in all the distances between one another first: O(n^2)
    for i in range(n):
        c1 = data[i]
        for j in range(i + 1, n):
            c2 = data[j]
            distance = dist(c1, c2)
            # distance = (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2
            heapq.heappush(heap, (distance, c1, c2))
    
    uf = UF(data)
    count = 1000
    while count > 0:
        _, c1, c2 = heapq.heappop(heap)
        uf.union(c1, c2)
        count -= 1

    end_time = time.time()
    print(f"Answer for part one: {uf.get_top3()}")
    print(f"Execution time for part one: {end_time - start_time:.6f} seconds")

    # can continue using the UF in part 2
    ans = 0
    while heap:
        _, c1, c2 = heapq.heappop(heap)
        uf.union(c1, c2)
        if uf.count == 1:
            ans = c1[0] * c2[0]
            break

    end_time = time.time()
    print(f"Answer for part two: {ans}")
    print(f"Execution time for part two: {end_time - start_time:.6f} seconds")

