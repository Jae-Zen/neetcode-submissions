class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freq = {};
        for (let num of nums) {
            freq[num] = (freq[num] ?? 0) + 1;
        }
        const heap = new MinPriorityQueue((x) => x[1])
        for (let item of Object.entries(freq)) {
            heap.enqueue(item);
            if (heap.size() > k) heap.dequeue();
        }
        const res = new Array(k);
        for (let i=0; i<k; i++) {
            res[i] = heap.dequeue()[0];
        }
        return res
    }
}
