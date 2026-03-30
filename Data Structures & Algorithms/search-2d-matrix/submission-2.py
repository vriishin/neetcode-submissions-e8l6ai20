class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix)-1
        mid = (lo+hi)//2

        while lo <= hi:
            
            if target>=matrix[mid][0] and target <= matrix[mid][-1]:
                return self.binarySearch(matrix[mid], target)
            
            if target<matrix[mid][0]:
                hi = mid -1
                mid = (lo+hi)//2
            
            if target>matrix[mid][-1]:
                lo = mid + 1
                mid = (lo+hi)//2
        
        return False

    
    def binarySearch(self, nums, target):
        lo, hi = 0, len(nums) - 1
        mid = (lo + hi)//2

        while lo<=hi:

            if nums[mid] == target:
                return True

            if nums[mid]< target:
                lo = mid+1
                mid = (lo + hi)//2 

            if nums[mid]> target:
                hi = mid -1
                mid = (lo + hi)//2

        return False