class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest= 0
        for num in nums:
            if num - 1 not in numSet: 
                nextnum = 0
                while (num+nextnum) in numSet:
                    nextnum+=1
                longest = max(nextnum,longest)
        return longest
        