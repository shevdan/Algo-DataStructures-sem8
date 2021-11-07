from typing import List


class Heap:
    def __init__(self, arr) -> None:
        self.arr = arr
        self.heap_size = len(self.arr)

    def left(self,idx):
        if idx == 0:
            return 1
        return 2*(idx + 1) - 1
    
    def right(self, idx):
        if idx == 0:
            return 2
        return 2* (idx + 1)

    def parent(self, idx):
        return (idx - 1) // 2

    def buildMaxHeap(self):
        for i in range(len(self.arr) // 2, -1, -1):
            self.maxHeapify(i)

    def maxHeapify(self, idx):
        left_son = self.left(idx)
        right_son = self.right(idx)
        if left_son < self.heap_size and self.arr[left_son].data >= self.arr[idx].data:
            largest = left_son
        else:
            largest = idx
        if right_son < self.heap_size and self.arr[right_son].data >= self.arr[largest].data:
            largest = right_son
        if largest != idx:
            self.arr[idx], self.arr[largest] = self.arr[largest], self.arr[idx]
            self.maxHeapify(largest)

    def extractMax(self):
        if self.heap_size < 0:
            return 0
        max_val = self.arr[0]
        self.arr[0], self.arr[self.heap_size - 1] = self.arr[self.heap_size - 1], self.arr[0]

        self.heap_size -= 1
        self.maxHeapify(0)
        return max_val

    def insert(self, val):
        self.heap_size += 1
        if self.heap_size > len(self.arr):
            self.arr.append(val)
        else:
            self.arr[self.heap_size - 1] = val
        idx = self.heap_size - 1
        while idx > 0 and self.arr[self.parent(idx)].data < self.arr[idx].data:
            self.arr[self.parent(idx)], self.arr[idx] = self.arr[idx], self.arr[self.parent(idx)]
            idx = self.parent(idx)


class Elm_with_idx:
    def __init__(self, data, idx) -> None:
        self.data = data
        self.idx = idx
    
    def __str__(self) -> str:
        return f"data={self.data}, idx={self.idx}"


def solve(arr: List[int], window: int):
    for idx in range(len(arr)):
        arr[idx] = Elm_with_idx(arr[idx], idx)
    start = 0
    max_lst = []
    heap = Heap(arr[start : (start + window)])
    heap.buildMaxHeap()
    max_lst.append(heap.arr[0].data)
    start += 1

    while start + window <= len(arr):
        while heap.arr[0].idx < start:
            heap.extractMax()
        heap.insert(arr[start + window - 1])
        max_lst.append(heap.arr[0].data)
        start += 1
    return max_lst


if __name__ == "__main__":
    lst = [i for i in range(100)]
    # lst =  [1,3,-1,-3,5,3,6,7]
    window = 15
    # print(lst)
    # lst2 = [i for i in range(15)]
    # print(lst2)

    # print(solve(lst, window))
    # lst2 = [5, 3, 8]
    # heap = Heap(lst2)
    # heap.buildMaxHeap()
    # print(heap.arr)

    print([i for i in range(1, 10)])
