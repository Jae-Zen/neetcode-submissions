class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freq = {};
        for (let num of nums) {    //O(n)
            freq[num] = (freq[num] ?? 0) + 1;
        }
        const bucket_arr = Array.from({ length: nums.length + 1}, () => []);
        for (let key of Object.keys(freq)) {
            bucket_arr[freq[key]].push(parseInt(key));
        }

        const res = [];
        for (let i=bucket_arr.length - 1; i>=0; i--) {
            for (let num of bucket_arr[i]) {
                res.push(num)
                if (res.length >= k) {
                    return res
                }
            }
        }
        


    }
}
