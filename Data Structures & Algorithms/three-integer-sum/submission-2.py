class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for i in range(len(nums)):
            freq[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                freq[nums[j]] -= 1
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                target = - (nums[i] + nums[j])
                if freq.get(target, 0) > 0:
                    res.append([nums[i], nums[j], target])
            for j in range(i + 1, len(nums)):
                freq[nums[j]] = freq.get(nums[j], 0) + 1
        return res