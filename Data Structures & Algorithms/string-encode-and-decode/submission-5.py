class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s = ' '.join(strs)
        return s


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        arr = s.split(" ")
        return arr
