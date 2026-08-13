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

        heap = [(k,0)]
      


        while heap: 
            node, w = heapq.heappop(heap)


            for num, weight in adj[node]:
                if dest[num-1] == float('inf'):
                    dest[num-1] = dest[node-1] + weight
                    heap.append((num, weight)) 
                if dest[num-1]>dest[node-1]+weight:
                    dest[num-1] = dest[node-1] + weight
                    heap.append((num, weight))
            print(heap)
            print(dest)
            

        res = -1   
        for i in range(len(dest)):
            if dest[i]==float('inf'):
                return -1
            res = max(res, dest[i]) 
        return int(res)
        
                
                

            


        