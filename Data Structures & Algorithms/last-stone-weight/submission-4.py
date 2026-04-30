class Solution:
        
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap) #makes this a max heap
        
        while len(heap)>1:
            val1 = -heapq.heappop(heap)
            val2 = -heapq.heappop(heap)

            if val1 == val2:
                continue
            else:
                new = abs(val1-val2)
                heapq.heappush(heap,-new)
        if len(heap)==0:
            return 0
        return -heap[0]



    # def sink(self, heap, heapsize, parent):
    #     while parent<heapsize: 
    #         l, r = 2*parent +1, 2*parent +2
    #         largest = parent

    #         if l<heapsize and heap[l]> heap[parent]:
    #             largest = l
            
    #         if r< heapsize and heap[r]> heap[largest]:
    #             largest = r 
            
    #         if largest == parent:
    #             return
            
    #         self.swap(parent, largest)
    #         parent = largest
    
    # def swap(self, p, q):
    #     self.heap[p], self.heap[q] = self.heap[q], self.heap[p]
        