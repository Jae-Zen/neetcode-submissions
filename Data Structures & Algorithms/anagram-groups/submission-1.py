class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            char_freq = [0] * 26
            for char in word:
                char_freq[ord(char) - ord("a")] += 1
            hashmap[tuple(char_freq)].append(word)
        return list(hashmap.values())
   
