
def solve(r_lst):
    r = sorted(r_lst, reverse=True)

    sum = 0
    for i in range(len(r)):
        sum += r[i] ** i
    
    return sum


if __name__ == "__main__":
    r = [1,2,3,4,5]
    print(solve(r))
