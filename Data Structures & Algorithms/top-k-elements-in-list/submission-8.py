class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        heap = []
        for item in freq.items():
            heapq.heappush(heap, (item[1], item[0]))
            if len(heap) > k:
                heapq.heappop(heap)
        res = [item[1] for item in heap]
        return res