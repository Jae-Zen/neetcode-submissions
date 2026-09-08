class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_zero = 1
        product_no_zero = 1
        res = []
        zero_counter = 0
        for num in nums:
            product_zero *= num
            if num == 0:
                zero_counter += 1
            else:
                product_no_zero *= num
        for num in nums:
            if num == 0:
                if zero_counter > 1:
                    res.append(0)
                else:
                    res.append(product_no_zero)
            else:
                res.append(int(product_zero / num))
        return res
        