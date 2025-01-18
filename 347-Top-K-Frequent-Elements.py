class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        arr = [[] for _ in range(len(nums) + 1)]
        ret = []

        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)
        
        for element, frequency in freq.items():
            arr[frequency].append(element)
        
        for i in range(len(arr) - 1, 0, -1):
            for num in arr[i]:
                ret.append(num)
                if len(ret) == k:
                    return ret
