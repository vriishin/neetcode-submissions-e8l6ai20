class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid),len(grid)
        heap = [(grid[0][0],0,0)]
        visited = set()

        while heap:
            t, r, c = heapq.heappop(heap)
            
            neighbors = [(r+1,c), (r-1, c), (r, c+1), (r,c-1)]
            
            if r == ROWS -1 and c == COLS-1:
                return t
            
            for nr, nc in neighbors:
                if min(nr,nc)<0 or nr == ROWS or nc == COLS or (nr,nc) in visited:
                    continue
                visited.add((nr,nc))
                heapq.heappush(heap, [max(t,grid[nr][nc]),nr,nc])
                