class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const records = {}
        for (let i=0; i<nums.length; i++) {
            let num_needed = target - nums[i];
            if (Object.hasOwn(records, nums[i])){
                return [records[nums[i]][1], i];
            } else {
                records[num_needed] = [nums[i], i];
            }
        }
    }
}
