class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset):
            if sum(subset) == target:
                if subset not in res:
                    res.append(subset[:])
                return
            if sum(subset)> target or i > len(nums):
                return

            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j+1, subset[:])
                subset.pop()
        
        dfs(0, [])
        return res