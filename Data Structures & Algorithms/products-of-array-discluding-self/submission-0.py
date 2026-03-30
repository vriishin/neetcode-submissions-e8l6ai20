class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1 
        sol = [1]*len(nums)
        for i in range(len(nums)):
            sol[i]= pre
            pre *= nums[i]

        post = 1
        for i in range(-1, -len(nums) - 1, -1):
            sol[i]*=post
            post *= nums[i]

        return sol