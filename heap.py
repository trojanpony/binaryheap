# my implementation of heap/heapsort


class HeapSort:
    def __init__(self, arr, low, high):
        self.low = low
        self.high = high

        # The original input array
        self.org_arr = arr

        # Store the indexes of the values to be sorted in a new array
        self.new_arr = [i for i in range(len(arr)) if (arr[i] > low) and (arr[i] < high)]
        

class BinaryHeap:
    def __init__(self):
        self.size = 0 
        self.heap = [(0)] 

    def percUp(self, i):
        # code example found on keon/algorithms on github.com
        while i // 2 > 0:
            if self.heap[i] > self.heap[i //2]:
                # swap the value of the parent with the child
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i // 2

    def insert(self, val):
        self.heap.append(val)
        self.size = self.size + 1
        self.percUp(self.size)

    def maxChild(self, i):
        # code example found on keon/algorithms on github.com
        if ((2*i)+1) > self.size: # no right child
            return 2*i 
        else:
            return True

    def removeMax(self):
        max = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size = self.size - 1
        self.heap.pop()
        self.percUp(1)
        return max
   
############################################
# For testing purposes
############################################
#test_data = [21,57,35,44,51,14,6,28,39,15]
#test = HeapSort(test_data, 20, 50)
#print(test.new_arr)
#for num in test.new_arr:
#   print(test.org_arr[num])
############################################

test_input = [int(val) for val in input('Enter a list seperated by ,:').split(',')]
low = int(input('Enter a low value:'))
high = int(input('Enter a high value:'))

test = HeapSort(test_input, low, high)
T = BinaryHeap()
for num in test.new_arr:
    T.insert(test.org_arr[num])

while T.size > 0:
    test.org_arr[test.new_arr.pop()] = T.removeMax()

print(test.org_arr)


