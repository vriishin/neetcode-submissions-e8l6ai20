class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 0
        r = len(nums) - 1
        sol = []

        while l<r:
            temp = []
            j = r
            for i in range(l,j):
                if nums[l]+nums[i]+nums[j] == 0:
                    temp = [nums[l],nums[i],nums[j]]
                    sol.append(temp)
                j-=1
            r-=1
            
        return sol           