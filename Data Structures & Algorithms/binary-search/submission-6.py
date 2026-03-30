class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0 
        hi = len(nums) - 1
        mid = int((lo + hi)/2)

        while lo<hi: 
            if target > nums[mid]:
                lo = mid +1
                mid = int((lo + hi)/2)
            
            if target< nums[mid]: 
                hi = mid - 1 
                mid = int((lo + hi)/2)
            
            if nums[mid] == target: break

        return mid if target==nums[mid] else -1


        