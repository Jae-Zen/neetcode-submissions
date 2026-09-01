class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            for char in string:
                res += chr((ord(char) + 40) % 255)
            res += '?'
        return res


    def decode(self, s: str) -> List[str]:
        string = ""
        res = []
        for char in s:
            print(char)
            if char == "?":
                res.append(string)
                string = ""
            else:
                string += chr((ord(char) - 40) % 256)
        return res
