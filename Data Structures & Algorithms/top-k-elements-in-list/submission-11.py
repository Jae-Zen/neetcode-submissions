class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:  #O(n)
            freq[num] = freq.get(num, 0) + 1
        freq_arr = [[] for _ in range(len(nums) + 1)]  #O(n)
        for item in freq.items():
            freq_arr[item[1]].append(item[0])  #O(n)
        res = []
        for numbers in freq_arr[::-1]:  #O(n)
            for num in numbers:
                res.append(num)
                if len(res) >= k:
                    return res
