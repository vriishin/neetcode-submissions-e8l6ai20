class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0],0,0)]
        
        visited = set()
        while heap:
            t, r, c = heapq.heappop(heap)
            neighbors = [(r+1, c), (r-1, c), (r, c-1), (r,c+1)]
            if r == n-1 and c == n-1:
                return t
            
            for nr, nc in neighbors:
                if min(nr,nc)<0 or nr == n or nc == n or (nr,nc) in visited:
                    continue
                
                heapq.heappush(heap,(max(t,grid[nr][nc]),nr,nc))
                visited.add((nr,nc))
            