class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 0
        r = len(nums) - 1
        nums.sort()
        sol = []
        
        while l<r:
            i=l+1
            r = len(nums) - 1
            if l!=0 and nums[l]==nums[l-1]:
                l+=1
                continue 
            

            while i<r:
                s = nums[l]+nums[i]+nums[r]

                
                if s>0:
                    r-=1
                elif s<0:
                    i+=1
                else:
                    sol.append([nums[l], nums[i], nums[r]])
                    i += 1
                    r -= 1
                    while i < r and nums[i] == nums[i - 1]:
                        i += 1
                    while i < r and nums[r] == nums[r + 1]:
                        r -= 1
            l+=1
        return sol           