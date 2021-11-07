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

    def maxHeapify(self, idx):
        '''
        Iterative implementation of maxHeapify
        '''

        while idx < self.heap_size:
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
                idx = largest
            else:
                break

if __name__ == "__main__":
    lst = [i for i in range(9)]
    print(lst)
    heap = Heap(lst)
    heap.maxHeapify(0)
    print(heap.arr)
