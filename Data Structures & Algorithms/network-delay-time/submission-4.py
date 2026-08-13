import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if n ==0:
            return -1

        adj = defaultdict(list)
        dest = [float('inf')] * n 
        dest[k-1] = 0

        for src, dst, w in times:
            adj[src].append((dst,w))
        print(adj)

        # CHANGE:
        # heap should store (total distance, node)
        # because Python's heap prioritizes the FIRST item
        heap = [(0,k)]
      
        while heap: 
            # CHANGE:
            # pop distance first, then node
            w, node = heapq.heappop(heap)

            # CHANGE:
            # We may have pushed this node into the heap earlier
            # with a worse distance. Skip that old entry.
            if w > dest[node-1]:
                continue

            for num, weight in adj[node]:
                if dest[num-1] == float('inf'):
                    dest[num-1] = dest[node-1] + weight

                    # CHANGE:
                    # heappush keeps the heap valid in O(log H).
                    # Also push TOTAL distance, not just edge weight.
                    heapq.heappush(heap, (dest[num-1], num))

                if dest[num-1]>dest[node-1]+weight:
                    dest[num-1] = dest[node-1] + weight

                    # CHANGE:
                    # Same thing here: push (total distance, node)
                    heapq.heappush(heap, (dest[num-1], num))

        res = -1   
        for i in range(len(dest)):
            if dest[i]==float('inf'):
                return -1
            res = max(res, dest[i]) 
        return int(res)

        
        # Original issue: the heap was prioritizing node number instead of total path distance.
        # I was also appending normally and calling heapify each loop, which rebuilt the heap in O(H).
        # Dijkstra should store (total_distance, node) and use heappush/heappop to maintain the heap in O(log H).
        # The heap also needs the full distance from k, not just the weight of the most recent edge.
            

        # if n ==0:
        #     return -1

        # adj = defaultdict(list)
        # dest = [float('inf')] * n 
        # dest[k-1] = 0

        # for src, dst, w in times:
        #     adj[src].append((dst,w))
        # print(adj)

        # heap = [(k,0)]
      


        # while heap: 
        #     node, w = heapq.heappop(heap)


        #     for num, weight in adj[node]:
        #         if dest[num-1] == float('inf'):
        #             dest[num-1] = dest[node-1] + weight
        #             heap.append((num, weight)) 
        #         if dest[num-1]>dest[node-1]+weight:
        #             dest[num-1] = dest[node-1] + weight
        #             heap.append((num, weight))
         
        #     heapq.heapify(heap)

        # res = -1   
        # for i in range(len(dest)):
        #     if dest[i]==float('inf'):
        #         return -1
        #     res = max(res, dest[i]) 
        # return int(res)
        
                
                

            


        