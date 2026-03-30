class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        s = s.lower()

        while l<r:
            while l<r and not self.isAlphanum(s[l]):
                l+=1
            while l<r and not self.isAlphanum(s[r]):
                r-=1
            if s[l] != s[r]:
                return False
            l+=1
            r-=1

        return True
    
    def isAlphanum(self, c):
        return (    (ord('0') <= ord(c) <= ord('9')) or 
                    (ord('a')<= ord(c) <= ord('z'))  )   