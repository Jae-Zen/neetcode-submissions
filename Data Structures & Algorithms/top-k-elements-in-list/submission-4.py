import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}
        for num in nums:
            hashtable[num] = hashtable.get(num, 0) + 1
        top_freq_arr = []
        for num, count in hashtable.items():
            if len(top_freq_arr) != k:
                heapq.heappush(top_freq_arr, (count, num))
            else:
                if count > top_freq_arr[0][0]:
                    heapq.heapreplace(top_freq_arr, (count,num))
            


        
       
        return [num for count, num in top_freq_arr]


