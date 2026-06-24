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

            subset.append(nums[i])
            dfs(i+1, subset, runningtotal + nums[i])
            subset.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1, subset, runningtotal)

            
        dfs(0, [], 0)
        return res