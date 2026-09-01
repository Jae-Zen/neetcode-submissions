class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        hashtable = {}
        for num in nums:
            hashtable[num] = hashtable.get(num, 0) + 1
        for num, count in hashtable.items():
            freq[count].append(num)
        K_freq = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                K_freq.append(num)
                if len(K_freq) == k:
                    return K_freq


