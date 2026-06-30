class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(idx): #dfs
            res.append(subset.copy())

            
            for j in range(idx, len(nums)):
                subset.append(nums[j])
                backtrack(j+1)
                subset.pop()
            
            
        backtrack(0)
        return res
           