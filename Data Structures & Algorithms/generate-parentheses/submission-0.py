class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def dfs(subset, n, closecount):
            if n == 0 and closecount == 0 :
                string = ''.join(subset)
                print(string)
                res.append(string)
                return
            
        
            if n>0:
                subset.append('(')
                dfs(subset[:], n-1, closecount+1)
                subset.pop()
            if closecount>0:
                subset.append(')')
                dfs(subset[:], n, closecount-1)
                subset.pop()

        dfs([], n,0)
        return res
            


