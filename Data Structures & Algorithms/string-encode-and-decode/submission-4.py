class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return []
        s = ' '.join(strs)
        return s


    def decode(self, s: str) -> List[str]:
        if len(s)==0:
            return [""]
        arr = s.split(" ")
        return arr
