class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        
        target = nums[0]
        while lo<hi:
            mid = (lo+hi)//2
       
            if nums[mid]>nums[hi]:
                lo = mid + 1
            if nums[mid]<nums[hi]:
                target = nums[mid]
                hi = mid
            
        return target