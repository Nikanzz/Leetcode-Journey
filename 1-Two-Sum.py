class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i in range(len(nums)):
            if nums[i] in differences:
                return [differences[nums[i]], i]
            dif = target - nums[i]
            differences[dif] = i
