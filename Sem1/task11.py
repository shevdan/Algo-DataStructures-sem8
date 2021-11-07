def fibsearch(arr, x):

    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2
    while fib < len(arr):
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1
    
    offset = -1

    while fib > 1:

        i = offset + fib2

        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i

        elif arr[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i


    if fib1 and arr[-1] == x:
        return len(arr) - 1
    return -1


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 9, 23, 73, 123]
    for i in range(len(arr)):

        print(fibsearch(arr, i))


