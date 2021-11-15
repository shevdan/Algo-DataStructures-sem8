n = int(input())
m = int(input())
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

a[0] = (a[0], "")
b[0] = (b[0], "")
for i in range(1,n):
    if a[i-1][0]+a[i] > b[i-1][0]+a[i]+m:
        a[i] = (b[i-1][0]+a[i]+m, 'B')
    else:
        a[i] = (a[i-1][0]+a[i], 'A')
    
    if b[i-1][0]+b[i] > a[i-1][0]+b[i]+m:
        b[i] = (a[i-1][0]+b[i]+m, 'A')
    else:
        b[i] = (b[i-1][0]+b[i], 'B')

res = ""
if a[n-1][0] > b[n-1][0]:
    res = "B"
else:
    res = "A"
for i in range(n-1,-1, -1):
    if res[0] == 'A':
        res = a[i][1] + res
    else:
        res = b[i][1] + res

print(res)