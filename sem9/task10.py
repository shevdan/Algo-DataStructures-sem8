def solve( s: str) -> int:
    n = len(s)
    palindromes =[[False for i in range(n)] for j in range(n)]
    for i in range(n):
        palindromes[i][i] = True
        if i != n-1 and s[i] == s[i+1]:
            palindromes[i][i+1] = True
    for j in range(2,n+1):
        for i in range(n-j):
            if s[i] == s[i+j] and palindromes[i+1][i+j-1]:
                palindromes[i][i+j] = True

    dp_matrix = [1]*n
    for i in range(1,n):
        res = float("inf")
        for j in range(0,i+1):
            if palindromes[j][i]:
                if j>=1:
                    res = min(res, dp_matrix[j-1])
                else: res = 0
        dp_matrix[i] = res+1
    return dp_matrix[n-1]-1


print(solve("xbcy"))