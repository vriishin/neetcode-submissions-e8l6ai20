class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force is a solution, but might not work with large arrays
        # hashmap, add each element to map one my one, check if diff between target and current num is in map. 

        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap: 
                return [prevMap[diff],i]
            prevMap[n] = i
        return