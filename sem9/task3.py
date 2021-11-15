# n = int(input())
# r = int(input())
# c = int(input())
# s = list(map(int,input().split(" ")))
n = 10
r = 1
c = 10
s = list(map(int,"12 12 12 12 12 12 12 12 9 11".split(" ")))
s = [0] + s

for i in range(1,n + 1):
    print(s)
    if i> 3:
        s[i] = min(s[i-4]+4*c, s[i-1]+s[i]*r)
    else:
        s[i] = s[i-1]+s[i]*r

print(s[n])