from math import floor
def partition(A, p, r):
    is_equal=True
    x = A[r]
    i=p-1

    for j in range(p, r):
        if A[j] != x:
            is_equal = False

        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]


    if is_equal:
        return floor((p + r) / 2) + 1
    
    A[i+1], A[r] = A[r], A[i+1]

    return i + 1


A = [5, 5, 6, 7, 5]
print(partition(A, 0, len(A) -1))