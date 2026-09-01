class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const s = new Set();
        for (const num of nums) {
            if (s.has(num)) {
                return true
            } else {
                s.add(num);
            }
        }
        return false
    }
}



