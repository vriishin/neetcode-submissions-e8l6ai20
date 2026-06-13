class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnts = Counter(tasks)
        sol = 0 
        highest = 0 
        numHighest = 0
        
        for num in cnts:
            if cnts[num]>highest:
                highest = cnts[num]
        for num in cnts:
            if cnts[num] == highest:
                numHighest += 1
        
        sol = (n + 1) * (highest -1 ) + numHighest
        return max(len(tasks), sol)
