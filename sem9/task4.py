n = int(input())
c = list(map(int, input().split(' ')))

dp_table = [[0 for i in range(n)]for j in range(n)]
dp_table[0][n-1] = (c[n-1],0)
last_min = (c[n-1],0)
for j in range(1,n):
    dp_table[0][n-1-j] = (last_min[0] + c[n-j-1], last_min[1])
    cur_min = (dp_table[0][n-1-j][0], 0)
    for i in range(1,j+1):
        dp_table[i][n-1-j] = (dp_table[i-1][n-j][0] + i, i-1)
        if dp_table[i][n-1-j][0] <  cur_min[0]:
            cur_min = (dp_table[i][n-1-j][0], i)

    last_min = cur_min

res = [False]*n
for j in range(n-1):
    if last_min[1] == 0:
        res[j] = True
    else:
        res[j] = False
    last_min = dp_table[last_min[1]][j]

res[n-1] = True
print(res)

