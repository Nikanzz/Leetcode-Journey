class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = 0
        ret = [0] * len(nums)

        for num in nums:
            if num:
                product *= num
            else:
                zero += 1
            if zero > 1:
                return ret
        
        for index, current in enumerate(nums):
            if zero:
                if nums[index] == 0:
                    ret[index] = product
            else:
                ret[index] = product//current
        return ret
