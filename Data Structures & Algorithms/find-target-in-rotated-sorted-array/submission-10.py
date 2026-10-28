class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1

        while lo<=hi: 
            mid = (lo+hi)//2
            if target==nums[mid]:
                return mid
            
            if nums[hi]>=nums[mid]:
                if nums[mid]<target<nums[hi]:
                    hi = mid -1 
                else:
                    lo = mid + 1

            else:
                if nums[mid]>target>nums[lo] :
                    lo = mid +1  
                else:
                    hi = mid - 1
         
        return -1

        