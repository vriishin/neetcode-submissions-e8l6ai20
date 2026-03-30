class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r = len(numbers) -1 

        while l<r: 
            goal = target - numbers[r]
            while l<r and numbers[l]<goal: 
                l+=1
            if numbers[l] +numbers[r]==target:
                return [l+1,r+1]
            
            r-=1
            