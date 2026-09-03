class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const records = new Map();
        for (let i=0; i<nums.length; i++) {
            const diff = target - nums[i];
            if (records.has(diff)) {
                return [records.get(diff), i]
            } else {
                records.set(nums[i], i)
            }
        }
        return []
        
    }
}
