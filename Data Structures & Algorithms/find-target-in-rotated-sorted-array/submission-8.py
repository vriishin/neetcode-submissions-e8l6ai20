class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1

        while lo<=hi: 
            mid = (lo+hi)//2
            if target==nums[mid]:
                return mid
            
            if nums[hi]>=nums[mid]:
                if target<=nums[hi] or target>nums[mid]:
                    hi = mid -1 
                else:
                    lo = mid + 1

            else:
                if target>=nums[lo] or target<nums[mid]:
                    lo = mid +1  
                else:
                    hi = mid - 1
            print(nums[mid])
        return -1

        