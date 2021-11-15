
def solve(r_lst):
    r = sorted(r_lst, reverse=True)

    first_idx = {}
    for i in range(len(r_lst)):
        first_idx[r_lst[i]] = i


    license = []
    for i in range(len(r)):
        license.append(first_idx[r[i]])
    
    return license


if __name__ == "__main__":
    r = [1,2,3,4,5]
    print(solve(r))
