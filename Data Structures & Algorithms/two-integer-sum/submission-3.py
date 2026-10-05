class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hist = dict()
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hist: return [hist[diff], i]
            hist[n] = i
        return []