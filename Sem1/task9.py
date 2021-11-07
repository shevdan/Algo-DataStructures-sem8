def coincidences(arr1: list, arr2: list) -> None:
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            print(arr1[i])
            i += 1
            j += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            i += 1

if __name__ == "__main__":
    arr1 = [1, 5, 12, 43, 67]
    arr2 = [2, 5, 7, 12, 42, 67, 223]
    coincidences(arr1, arr2)