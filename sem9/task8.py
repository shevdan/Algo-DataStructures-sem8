

def solve(lst: list):
    minprod, maxprod = lst[0], lst[0]
    res = lst[0]

    for num in lst[1:]:
        
        minprod, maxprod = (min(minprod * num, maxprod * num, num), 
                                max(minprod * num, maxprod * num, num))
        res = max(maxprod, res)
    return res


if __name__ == '__main__':
    lst = [4, 5, -3, 6]
    print(solve(lst))

