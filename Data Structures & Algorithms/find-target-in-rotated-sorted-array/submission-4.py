class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1

        while lo<hi: 
            mid = (lo+hi)//2
            if target==nums[mid]:
                return mid
            
            if target>nums[mid]:
                if target<=nums[hi]:
                    lo = mid+1
                else:
                    hi = mid -1

            if target < nums[mid]:
                if target>=nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            
        return -1

        