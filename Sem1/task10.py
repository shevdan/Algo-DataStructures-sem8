

def merge(left, right, sorted_lst):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_lst[k] = left[i]
            i += 1
        else:
            sorted_lst[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        sorted_lst[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        sorted_lst[k] = right[j]
        j += 1
        k += 1
    
    return sorted_lst


def mergesort(arr: list):
    if len(arr) > 1:
        mid = len(arr) // 2
        left, right = mergesort(arr[:mid]), mergesort(arr[mid:])
        return merge(left, right, arr)
    return arr

def min_pair_arr(arr):
    arr = mergesort(arr)
    min_pair = abs(arr[1] - arr[0]), arr[1], arr[0]
    for i in range(1, len(arr)):
        dist = abs(arr[i] - arr[i - 1])
        if dist < min_pair[0]:
            min_pair = dist, arr[i - 1], arr[i] 
    return min_pair[1:]

if __name__ == "__main__":
    arr = [6,2, 1,9, 3, 0, 5, 23 , 73, 123, 4]
    print(mergesort(arr))
    print(min_pair_arr(arr))