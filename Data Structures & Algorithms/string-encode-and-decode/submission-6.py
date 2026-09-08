class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for string in strs:
            length = len(string)
            res += str(length) + '#' + string
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        start = 0
        i = 0
        while i < len(s):
            if s[i] == '#':
                length = int(s[start: i])
                res.append(s[i + 1: i + 1 + length])
                start = i + 1 + length
                i = start
            i += 1
        return res
