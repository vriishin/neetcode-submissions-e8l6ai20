import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        mid = int((lo+hi)/2)
        counter = 0
        lim = math.log2(len(nums))


        while nums[mid] != target and counter <= lim:
            if nums[mid]<target:
                lo = mid +1
                mid = int((lo+hi)/2)
            if nums[mid]>target:
                hi = mid -1 
                mid = int((lo+hi)/2)
            
            counter+=1

        
        if nums[mid] == target:
            return mid
        else:
            return -1