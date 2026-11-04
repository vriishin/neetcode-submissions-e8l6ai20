class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #backtracking problem

        res = set()

        def dfs(num,build):
            if len(build)==len(nums):
                res.add(tuple(build))
                return
            
            for i in range(len(num)):
                build.append(num[i])
                if i == len(num)-1:
                    dfs(num[:i],build)
                else:
                    dfs(num[:i] + num[i+1:],build)
                build.pop()
        
        dfs(nums, [])
        return list(res)