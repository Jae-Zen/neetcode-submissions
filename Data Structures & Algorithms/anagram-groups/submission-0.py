class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        output = []
        for word in strs:
            char_freq = [0] * 26
            for char in word:
                char_freq[ord(char) - ord("a")] += 1
            char_freq = tuple(char_freq)
            if char_freq in hashmap:
                hashmap[char_freq].append(word)
            else:
                hashmap[char_freq] = [word]
        for i in hashmap.values():
            output.append(i)
        return output
   
