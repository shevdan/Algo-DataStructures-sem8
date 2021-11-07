def insert_index(arr, element):
    lower=0
    higher = len(arr)
    while lower<higher:
        middle= (lower+higher)//2
        if arr[middle]<element:
            lower= middle+1
        else:
            higher=middle
    return lower


def find_insertion(arr, element):
    i = insert_index(arr, element)
    if i:
        return i-1
    return -1

def left_max(arr):
    res = [-1 for i in range(len(arr))]
    lst = [arr[0]]
    for i in range(1, len(arr)):
        index = find_insertion(lst, arr[i])
        if(index != -1):
            res[i] = lst[index]
 
        lst.insert(index+1 , arr[i])

    print(res)
    print(lst)
 

if __name__ == '__main__':
    arr = [7, 7, 1, 3, 3]
    left_max(arr)
