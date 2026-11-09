class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # calc distance to each point first then create adj list bc every point is a neighbor. O(m*n) time
        
        heap = []
        costs = {}
        adj = defaultdict(list)
        
        points.sort()
        if points:
            heapq.heappush(heap, (0, (points[0][0],points[0][1])))
        visited = set()
     
        #build adj list
        for x1, y1 in points:
            costs[(x1,y1)] = float('inf')
            for x2, y2 in points:
                if x1==x2 and y1==y2:
                    continue
                dist = abs(x1 - x2) + abs(y1 -y2)
                adj[(x1,y1)].append((dist, (x2,y2)))
                adj[(x2,y2)].append((dist, (x1,y1)))
        costs[(points[0][0],points[0][1])] = 0 

        while heap:
            path, (x,y) = heapq.heappop(heap)
            if (x,y) in visited:
                continue
            visited.add((x,y))    
            #for neighbors in adj[point]
            for cost, (xn,yn) in adj[(x,y)]:
                if (xn, yn) in visited:
                    continue

                if cost<costs[(xn,yn)]:  
                    heapq.heappush(heap,(cost,(xn,yn)))
                    costs[(xn,yn)] = cost

      
            
        res = 0
        for cost in costs.values():
            res+=cost
        return res

        #given points=[[0,0],[2,2],[3,3],[2,4],[4,2]]
        