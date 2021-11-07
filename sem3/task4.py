from collections import deque 

def partition(a, start, end):
    pivot = a[end]
    pIndex = start
    for i in range(start, end):
        if a[i] <= pivot:
            a[i], a[pIndex] = a[pIndex], a[i]
            pIndex = pIndex + 1
    a[pIndex], a[end] = a[end], a[pIndex]
    return pIndex


def iterativeQuicksort(a):
    stack = deque()
    start = 0
    end = len(a) - 1
    stack.append((start, end))
    while stack:
        start, end = stack.pop()
        pivot = partition(a, start, end)
        if pivot - 1 > start:
            stack.append((start, pivot - 1))
        if pivot + 1 < end:
            stack.append((pivot + 1, end))


if __name__ == '__main__':
    a = [5, 4, 1, 8, 5, 9, 1, 1, 15, 6, 8, 3]
    iterativeQuicksort(a)
    print(a)
