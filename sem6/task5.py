

def pairs(lst):
    dct = {}
    res = set()

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            prod = lst[i] * lst[j]
            if prod not in dct:
                dct[prod] = (lst[i], lst[j])
            else:
                res.add((dct[prod], (lst[i], lst[j])))

    
    return res

if __name__ == "__main__":
    lst = [1, 6, 3, 9, 2, 10]

    print(pairs(lst))
