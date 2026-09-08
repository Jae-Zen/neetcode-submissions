class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):  #calculating pre-fix  [1,1,2,8]
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):    #adding post-fix on top of [1,1,2,8]. post-fix=[48,24,6,1]  --> [48,24,12,8]
            res[i] *= postfix
            postfix *= nums[i]
        return res