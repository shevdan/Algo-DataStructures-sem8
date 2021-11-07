
class PriorityElm:
    def __init__(self, data, priority) -> None:
        self.data = data
        self.priority = priority

class PriorityHeap:
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
        if left_son < self.heap_size and self.arr[left_son].priority >= self.arr[idx].priority:
            largest = left_son
        else:
            largest = idx
        if right_son < self.heap_size and self.arr[right_son].priority >= self.arr[largest].priority:
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
        return max_val.data


    def insert(self, val, priority):
        self.heap_size += 1
        if self.heap_size > len(self.arr):
            self.arr.append(PriorityElm(val, priority))
        else:
            self.arr[self.heap_size - 1] = PriorityElm(val, priority)
        idx = self.heap_size - 1
        while idx > 0 and self.arr[self.parent(idx)].priority < self.arr[idx].priority:
            self.arr[self.parent(idx)], self.arr[idx] = self.arr[idx], self.arr[self.parent(idx)]
            idx = self.parent(idx)


class Stack:
    def __init__(self) -> None:
        self.heap = PriorityHeap([])
        self.priority = 0

    def push(self, elm, priority=None) -> None:
        if priority is None:
            priority = self.priority
            self.priority += 1

        self.heap.insert(elm, priority)
    
    def pop(self) -> int:
        try:
            return self.heap.extractMax()
        except IndexError as err:
            raise IndexError("Empty stack") from err



if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    
