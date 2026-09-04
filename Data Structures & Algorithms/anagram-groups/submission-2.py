class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        records = {}
        output = []
        for string in strs:
            freq = [0] * 26
            for char in string:
                char_index = (ord(char) - ord('a'))
                freq[char_index] += 1
            freq_tuple = tuple(freq)
            records[freq_tuple] = records.get(freq_tuple, []) + [string]
        
        return list(records.values())
