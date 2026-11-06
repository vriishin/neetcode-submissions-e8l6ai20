class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        adj = defaultdict(list)

        for src, dst, weight in times:
            adj[src].append((weight, dst))
        

        dist=[float('inf')]*n
        dist[k-1] = 0 

        heapq.heappush(heap, (0,k))
        total = 0
       
        while heap:
            path, node = heapq.heappop(heap)

            for extrad, nei in adj[node]:
                if path+extrad < dist[nei-1]:
                    dist[nei-1] = path+extrad
                    heapq.heappush(heap, (dist[nei-1], nei))
 
                
                
            




        for i in range(n):
            if dist[i] == float('inf'):
                return -1
            total = max(dist[i],total)
        return total