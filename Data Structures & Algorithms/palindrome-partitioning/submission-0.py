class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curPart = []

        def isPalindrome(string):
            for i in range(len(string)):
                if string[i] == string[-i-1]:
                    continue
                else:
                    return False
            return True

        def dfs(i):
            if i >= len(s):
                res.append(curPart.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    curPart.append(s[i:j+1])
                    dfs(j+1)
                    curPart.pop()

        dfs(0)
        return res      