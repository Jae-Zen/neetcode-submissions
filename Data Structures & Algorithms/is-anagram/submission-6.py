class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            d[t[i]] = 1 + d.get(t[i], 0)
            d[s[i]] = d.get(s[i], 0) - 1
        for value in d.values():
            if value != 0:
                return False
        return True
        
        
