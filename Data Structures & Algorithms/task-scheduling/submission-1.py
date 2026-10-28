class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnts = Counter(tasks)
        sol = 0 
        highest = 0 
        numHighest = 0
        if n == 1:
            return len(tasks)
        for num in cnts:
            if cnts[num]>highest:
                highest = cnts[num]
        for num in cnts:
            if cnts[num] == highest:
                numHighest += 1
        
        sol = (n + 1) * (highest -1 ) + numHighest
        return sol 
