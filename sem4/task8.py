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
        if left_son < self.heap_size and self.arr[left_son] >= self.arr[idx]:
            largest = left_son
        else:
            largest = idx
        if right_son < self.heap_size and self.arr[right_son] >= self.arr[largest]:
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

    def game(self):
        while self.heap_size > 1:
            max_val = self.extractMax()
            if self.arr[0] == max_val:
                self.extractMax()
            else:
                self.arr[0] -= max_val
                self.maxHeapify(0)
        return self.heap_size


def solve(arr: List[int]) -> bool:
    heap = Heap(arr)
    heap.buildMaxHeap()
    return heap.game()


if __name__ == "__main__":
    import random
    import time



    lst = [random.randint(-1000, 1000) for _ in range(100000)]
    # lst = [39, 22, 12, 33, 87, 19, 22, 50, 16, 44]
    # lst = [2,7,4,1,8,1]
    # lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(lst)
    # heap = Heap(lst)
    # heap.maxHeapify(0)
    # print(heap.arr)

    # heap = Heap(lst)
    # heap.buildMaxHeap()
    # print(heap.arr)
    # print(heap.extractMax())
    # print(heap.arr)
    # print(heap.extractMax())
    # print(heapsort(lst))
    now = time.time()
    print(solve(lst))
    print(time.time() - now)
