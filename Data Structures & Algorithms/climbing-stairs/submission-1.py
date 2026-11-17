class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1]= 1
        memo[2]=2

        def stairs(num):
            if num in memo:
                return memo[num]
            if num ==1:
                return memo[1]
            if num ==2: 
                return memo[2]
            
            fib = stairs(num-1) + stairs(num-2)
            memo[num]=fib
            return memo[num]
            # start at height and go down
        
        stairs(n)
        return memo[n]


            


