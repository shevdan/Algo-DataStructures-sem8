def solve(lst):

    lst = sorted(lst, key=lambda x: x[0])
    cnt = 0
    prev = -10**9

    for elm in lst:
        if elm[0] < prev:
            prev = min(elm[1], prev)
            cnt += 1
        else:
            prev = elm[1]
    
    return cnt



if __name__ == "__main__":
    lst = [[1,10],[12,15],[18,20],[5,25]]
    # lst2 = [[-5,5],[-5,5],[-5,5]]
    lst = [[1,2],[2,3],[3,4],[1,3]]

    print(solve(lst))
    # print(solve(lst2))