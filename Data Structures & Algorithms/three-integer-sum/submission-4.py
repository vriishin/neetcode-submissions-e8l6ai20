class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 0
        r = len(nums) - 1
        sol = []
        nums.sort()


        while l<r:
            temp = []
            

            if l != 0 and nums[l] == nums[l-1]:
                continue 
            


            while i<r:
                if nums[i] == nums[l]:
                    i+=1
                    continue
                
                s = nums[l]+nums[i]+nums[j]

                if s == 0:
                    temp = [nums[l],nums[i],nums[j]]
                    sol.append(temp)
               
            l= i
                
            r-=1
            
        return sol           