class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        memo[0]= cost[0]
        memo[1]= cost[1]


        def dfs(i):
            if i in memo:
                return memo[i]
            
            memo[i]= cost[i] + min(dfs(i-1),dfs(i-2))
            return memo[i]

        n = len(cost)
        return min(dfs(n-1), dfs(n-2))