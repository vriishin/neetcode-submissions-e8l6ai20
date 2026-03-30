from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))

        
        

    def get(self, key: str, timestamp: int) -> str: 
        lo, hi = 0, len(self.timemap[key])-1
        candidate = ''
        while lo<=hi:
            mid = (lo+hi)//2
            if self.timemap[key][mid] and self.timemap[key][mid][1] == timestamp:
                return self.timemap[key][mid][0]


            if self.timemap[key][mid][1]<timestamp:
                candidate = self.timemap[key][mid][0]
                lo = mid + 1
            else:
                hi = mid - 1
        return candidate



        
