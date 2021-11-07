def solve(lst):

    lst = sorted(lst, key=lambda x: x[0])
    cnt = 0
    prev = lst[0]

    for elm in lst:
        if elm[0] < prev[1]:
            lst.remove(elm)
            cnt += 1
        prev = elm
    
    return cnt



if __name__ == "__main__":
    lst = [[1,10],[12,15],[18,20],[5,25]]
    lst2 = [[-5,5],[-5,5],[-5,5]]

    print(solve(lst))
    print(solve(lst2))