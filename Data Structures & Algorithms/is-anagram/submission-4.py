class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = dict()
        d_t = dict()
        for letter in s:
            flag = d_s.get(letter)
            if flag:
                d_s[letter] += 1
            else:
                d_s[letter] = 1
        for letter in t:
            flag = d_t.get(letter)
            if flag:
                d_t[letter] += 1
            else:
                d_t[letter] = 1
        return d_t==d_s
        
