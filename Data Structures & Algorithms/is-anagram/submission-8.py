class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = {}
        d_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            d_t[t[i]] = 1 + d_t.get(t[i], 0)
            d_s[s[i]] = 1 + d_s.get(s[i], 0)
        return d_t == d_s
        
        
