class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_hash = {}
        freq_list = [[] for i in range(len(nums) + 1)]
        for num in nums:
            freq_hash[num] = freq_hash.get(num, 0) + 1
        for num, count in freq_hash.items():
            freq_list[count].append(num)
        res = []
        for i in range(len(nums), -1, -1):
            if len(res) >= k:
                return res
            for x in freq_list[i]:
                res.append(x)
        