# my implementation of heap/heapsort

my_arr = [21,57,35,44,51,14,6,28,39,15]

class BinaryHeap:
    
    def __init__(self):
        self.heap = [ ]
        self.min = None
        self.max = None
        self.sorted = []

    def insert(self, val):
        self.heap.append(val)

    def delete(self, val):
        pass

    def buildHeap(self, arr):
        temp_arr = []
        # Takes an array as input and builds the heap
        while len(arr) != 0:
            temp_arr.append(arr.pop())

        self.heap = temp_arr
    
    def heapify(self):
        pass

    def Print(self):
        size = len(self.heap)
        for i in range(size//2+1):
            print(self.heap[i])
            print('{}'.format('^', '^'))

heap = BinaryHeap()
heap.buildHeap(my_arr)
heap.Print()
