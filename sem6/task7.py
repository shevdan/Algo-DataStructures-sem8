from typing import List
from collections import defaultdict
from math import sqrt


def solve(points: List[List[int]]) -> int:
    def distance(a, b):
        distance = (points[a][0] - points[b][0])**2 + (points[a][1] - points[b][1])**2
        return sqrt(distance)

    pairs = 0
    d = defaultdict(list)
    length = len(points)

    for i in range(1, length):
        for j in range(0, i):
            curr_dist = distance(i, j)

            if curr_dist in d:
                for a, b in d[curr_dist]:
                    if a in (i, j) or b in (i, j):
                        pairs += 1
            
            #not (i, j), because order matters
            d[curr_dist].append((j, i))
    
    return pairs*2

if __name__ == "__main__":
    points = [[0,0],[1,0],[2,0]]
    print(solve(points))
