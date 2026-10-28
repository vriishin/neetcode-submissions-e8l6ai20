class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1

        while lo<hi: 
            mid = (lo+hi)//2
            if target==nums[mid]:
                return mid
            
            if target<nums[mid]:
                lo = mid+1  
            elif target<nums[mid] and target>nums[lo]:
                hi = mid 
            elif target>nums[mid] and target<nums[hi]:
                lo = mid + 1
            else: 
                hi = mid 
            
        return -1

        