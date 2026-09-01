import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}
        for num in nums:
            hashtable[num] = hashtable.get(num, 0) + 1
        freq_arr = []
        for num, count in hashtable.items():
            freq_arr.append((count, num))
        top_freq_arr = freq_arr[:k]
        heapq.heapify(top_freq_arr)
        for count, num in freq_arr[k:]:
            if count > top_freq_arr[0][0]:
                heapq.heapreplace(top_freq_arr, (count,num))
        i = 0
        for count, num in top_freq_arr:
            top_freq_arr[i] = num
            i += 1
        return top_freq_arr


