from typing import List

def solve(arr: List[int]) -> int:
        
    mi, n = arr[:], len(arr) 
    
    for i in range(n - 2, -1, -1):
        mi[i] = min(mi[i + 1], arr[i])
    
    res = 1
    m = 0
    for i in range(n - 1):
        m = max(m, arr[i])
        if m <= mi[i + 1]:
            res += 1
        
    return res

print(solve([4,3,8,9,9]))  