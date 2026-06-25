class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        track = [False]*len(nums)
        def dfs(subset):
            if len(subset)>=len(nums):
                res.append(subset[:])
                return

            for j in range(len(nums)):

                if track[j] == False:
                    subset.append(nums[j])
                    track[j] = True
                    dfs(subset)
                    subset.pop()
                    track[j] = False

        
        dfs([])
        return res