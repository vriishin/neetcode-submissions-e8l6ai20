class KthLargest:


    def __init__(self, k: int, nums: List[int]):
        self.k = k                                  # FIX: needed in add()
        self.heap = nums
        heapsize = len(self.heap)
        for i in range((heapsize//2)-1, -1, -1):
            self.sink(self.heap, heapsize,i)
        
        while len(self.heap)>k:
            self.pop(self.heap, 0)                  # FIX: heap-pop the root, not list-pop a leaf

        
    def add(self, val: int) -> int:
        self.heap.append(val)
        self.swim(self.heap, len(self.heap))
        if len(self.heap) > self.k:                 # FIX: maintain size-k
            self.pop(self.heap, 0)
        return self.heap[0]                         # FIX: return the kth largest
        
    def sink(self, heapArr, heapsize, parent):
        while parent < heapsize:
            l, r = 2 * parent + 1, 2*parent + 2
            smallest = parent

            if l < heapsize and heapArr[parent]>heapArr[l]:
                smallest = l 

            if r< heapsize and heapArr[smallest]>heapArr[r]:
                smallest = r
            if parent == smallest:
                return
            self.swap(parent, smallest)                
            parent = smallest
            
    def swim(self, arr, heapsize):
        
        leafIndex = heapsize - 1

        while leafIndex>0:
            parent = (leafIndex-1)//2               # FIX: parent of CURRENT node, not frozen
            if arr[leafIndex] < arr[parent]:        # FIX: min-heap → smaller swims up
                self.swap(leafIndex, parent)
                leafIndex = parent
            else:
                break

    def swap(self, smaller, larger): #smaller and larger are indices of smaller num and larger num in heap array
        self.heap[smaller], self.heap[larger] = self.heap[larger], self.heap[smaller]

    def heapify(self, array, heapsize, rootindex):
        left, right = 2*rootindex+1, 2*rootindex + 2 # 0 indexed so +1 and +2 == 2k and 2k+1 (1-indexed) for l and r 
        largest = rootindex #largest has to be an index, not the actual number 

        if left < heapsize and array[left]>array[rootindex]:
            largest = left
        
        if right < heapsize and array[right] > array[largest]:
            largest = right
        
        if largest != rootindex:
            self.swap(rootindex, largest)
            self.heapify(array, heapsize, largest)


    def pop(self, heap, topInd):
        self.swap(topInd, len(self.heap)-1)

        val = self.heap.pop()
        self.sink(self.heap, len(self.heap),0)
        return val