from typing import List


def solve(prices: List[int]) -> int:
    
    n = len(prices)
    i = 0
    p = 0

    while i < n - 1:
        # determines the local min
        while i < n - 1 and prices[i + 1] <= prices[i]:
            i += 1
            
        ss = i
        
        # determines local max
        while i < n - 1 and prices[i + 1] > prices[i]:
            i += 1
            
        p += prices[i] - prices[ss]
        
    return p

print(solve([5,10,15,20]))