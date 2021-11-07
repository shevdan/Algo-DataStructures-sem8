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
        if left_son < self.heap_size and self.arr[left_son].freq >= self.arr[idx].freq:
            largest = left_son
        else:
            largest = idx
        if right_son < self.heap_size and self.arr[right_son].freq >= self.arr[largest].freq:
            largest = right_son
        if largest != idx:
            self.arr[idx], self.arr[largest] =  self.arr[largest], self.arr[idx]
            self.maxHeapify(largest)
    
    def extractMax(self):
        if self.heap_size < 0:
            raise IndexError("Empty heap")
        max_val = self.arr[0]
        self.arr[0], self.arr[self.heap_size - 1] = self.arr[self.heap_size - 1], self.arr[0]

        self.heap_size -= 1
        self.maxHeapify(0)
        return max_val



class FreqElm:
    def __init__(self, data, freq=0) -> None:
        self.data = data
        self.freq = freq

def solve(arr: List[int]) -> int:
    freq_table = {}
    for elm in arr:
        if elm in freq_table:  #O(n)
            freq_table[elm] += 1
        else:
            freq_table[elm] = 1
    
    freq_arr = []
    for elm in freq_table:  #O(n)
        freq_arr.append(FreqElm(elm, freq_table[elm]))
    
    heap = Heap(freq_arr)
    heap.buildMaxHeap() #o(n)
    arr_length = len(arr)
    new_arr_length = 0
    num_elm_to_delete = 0
    while new_arr_length * 2 < arr_length:  #max O(n)
        new_arr_length += heap.extractMax().freq    #O(lgn)
        num_elm_to_delete += 1
    
    return num_elm_to_delete       #O(nlogn)

if __name__ == "__main__":
    lst = [1,2,3,4,5, 6, 7, 8, 9]
    print(solve(lst))
