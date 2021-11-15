
import random
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
            self.arr[idx], self.arr[largest] =  self.arr[largest], self.arr[idx]
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
        while idx > 0 and self.arr[self.parent(idx)] < self.arr[idx]:
            self.arr[self.parent(idx)], self.arr[idx] = self.arr[idx], self.arr[self.parent(idx)]
            idx = self.parent(idx)



# def left_max(lst):
#     dct = {}
#     dct[0] = -1

#     for i in range(1, len(lst)):
#         curr_max = max(lst[i - 1], dct[i - 1])
#         if curr_max < lst[i]:
#             dct[i] = curr_max
#         else:
#             dct[i] = dct[]


if __name__ == "__main__":
    lst = [2, 4, 3, 1, 5, 2]

    res = [-1, 2, 2, -1, 4, 1]