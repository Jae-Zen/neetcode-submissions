class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res
        
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        j = 0
        while i < len(s):
            
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            res.append(s[j + 1: j + length + 1])

            i = j + length + 1
            j = i
        return res
