class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for point in points:
            euclidean_distance = math.sqrt((0-point[0])**2 + (0-point[1])**2)
            heap.append([euclidean_distance, point])
        heapq.heapify(heap)
        print(heap)
        sol = []
        for i in range(k):
            val = heapq.heappop(heap)
            sol.append(val[1])
        return sol