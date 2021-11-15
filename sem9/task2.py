n = int(input())
x = list(map(int, input().split(' ')))
s = list(map(int, input().split(" ")))

dp_table = [[0 for i in range(n)] for j in range(n)]
dp_table[0][0], dp_table[0][1] = min(x[0],s[0]), min(x[1],s[0])
for i in range(2,n):
    dp_table[0][i] = dp_table[0][i-2] + min(x[i],s[0])

for i in range(1,n):
    for j in range(i, n):
        dp_table[i][j] = dp_table[i-1][j-1] + min(x[j],s[i])

print(dp_table)

maximum = float("-inf")
for i in range(n):
    maximum = max(maximum, dp_table[i][n-1])

print(maximum)