


def max_plan(a, b, time):
    # if given time is less then the list of comments at
    # given minute, return none
    if time >= len(a) or time >= len(b):
        return None
    # if time is none, return just maximum value
    if time == 1:
        return max(a[0], b[0])
    # get maximum from previous time and current one
    # for each machine
    max_a = max(max_plan(a, b, time - 1) + a[time], max_plan(b, a, time - 1))
    max_b = max(max_plan(b, a, time - 1) + b[time], max_plan(a, b, time - 1))
    # return the largest value
    return max(max_a, max_b)

if __name__ == "__main__":
    n = 2
    a = [1, 3, 5, 6, 2, 5, 9, 1]
    b = [9, 7, 4, 8, 2, 3, 9, 3]
    print(max_plan(a, b, n))