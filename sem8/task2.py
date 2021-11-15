def events(S, S_1):
    cnt = 0
    j = 0
    for i in range(len(S)):
        if S[i] == S_1[j]:
            j += 1
            cnt += 1
    
    return cnt == len(S_1)

print(events("ABCBD", "BCBD"))

