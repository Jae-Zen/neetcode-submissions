class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freq = {};
        for (let num of nums) {
            freq[num] = 1 + (freq[num] ?? 0);
        }
        const arr = Object.entries(freq);
        const arr_sort = arr.sort((a,b) => b[1] - a[1]);
        return arr_sort.slice(0, k).map(([num, freq]) => parseInt(num))
    }
}
