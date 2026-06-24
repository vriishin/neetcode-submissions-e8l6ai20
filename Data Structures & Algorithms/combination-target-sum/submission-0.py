class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        count = [0] *len(nums)
        for i in range(len(nums)):
            count[i] = target//nums[i]

        def dfs(i, subset):
            if sum(subset) == target:
                res.append(subset[:])
                return
            if sum(subset)> target:
                return
            if i >= len(nums):
                return 

            for j in range(i, len(nums)):
                if count[j]>0:
                    count[j]-=1 
                    subset.append(nums[j])
                    dfs(j, subset[:])
                    subset.pop()
                    count[j]+=1
                else:
                    subset.append(nums[j])
                    dfs(j+1,subset[:])
                    subset.pop()
        
        dfs(0, [])
        return res