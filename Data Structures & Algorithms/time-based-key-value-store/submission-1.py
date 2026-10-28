from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key = key
        self.value = value if value else ''
        self.timestamp = timestamp
        self.timemap[self.key].append((self.value, self.timestamp))

        
        

    def get(self, key: str, timestamp: int) -> str: 
        lo, hi = 0, len(self.timemap[key])-1

        while lo<=hi:
            mid = (lo+hi)//2
            if self.timemap[key][mid] and self.timemap[key][mid][1] == timestamp:
                return self.timemap[key][mid][0]
            else:
                return self.timemap[key][mid-1][0] 

                # if len(self.timemap[key][mid])>1:
                #     return self.timemap[key][mid-1][0]
                # else: break



            if self.timemap[key][mid][1]<timestamp:
                lo = mid + 1
            else:
                hi = mid - 1
        return ''



        
