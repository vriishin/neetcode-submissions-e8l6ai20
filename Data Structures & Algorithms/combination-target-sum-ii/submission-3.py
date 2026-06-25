class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, subset, runningtotal):
            if runningtotal == target:
                res.append(subset[:])
                return
            if runningtotal> target or i >= len(nums):
                return
            for j in range (i, len(nums)):
                if j>i and nums[j] == nums[j-1]:
                    continue
                subset.append(nums[j])
                dfs(j+1, subset, runningtotal + nums[j])
                subset.pop()
                

            
        dfs(0, [], 0)
        return res