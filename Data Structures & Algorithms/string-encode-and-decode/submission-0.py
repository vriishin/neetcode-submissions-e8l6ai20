class Solution:

    def encode(self, strs: List[str]) -> str:
        
        s = ' '.join(strs)
        return s


    def decode(self, s: str) -> List[str]:
        arr = s.split(" ")
        return arr
