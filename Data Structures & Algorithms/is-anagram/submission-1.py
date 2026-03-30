class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = defaultdict(int)
        countT = defaultdict(int)
        for letter in s:
            countS[letter]+=1
            # add letter as key and count of letter as value
        for letter in t:
            countT[letter]+=1
            # do the same as above
        
        #compare letter counts in s and t
        for letter in (countS and countT):
            if countS[letter] != countT[letter]:
                return False
        
        if len(countS) == len(countT):
            return True
        
        return False 

        #another solution is to sort both strings and compare them to see if theyre equal  
