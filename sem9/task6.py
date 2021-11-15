
def solve(coords: list):
    time = len(coords)
    curr_coord = coords[-1]
    res = 0
    memo = {}

    
    def recurse(coords, time, curr_coord, j):
        if j == -1:
            if time >= abs(coords[j + 1]):
                return 1 + res
            else:
                return res

        time_to_move = abs(coords[j] - curr_coord)
        if time - time_to_move < 0:
            return max(res, memo.get((j, time, curr_coord), recurse(coords, time, curr_coord, j - 1)))
        else:

            return max(res, max(memo.get((j, time, curr_coord), recurse(coords, time, curr_coord, j - 1)), 
                1 + memo.get((j - 1, time - time_to_move, coords[j]), recurse(coords, time - time_to_move, coords[j], j-1))))
    

    return recurse(coords, time, curr_coord, len(coords) - 2)





if __name__ == "__main__":
    lst = [-1, 2, 3, 2]
    for i in range(len(lst)):
        print(lst[i], i)
    print(solve(lst))