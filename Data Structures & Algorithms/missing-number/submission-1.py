class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # better solution with XOR
        i = 0
        nums.sort()
        while i < len(nums):
            if nums[i] != i:
                return i
            i += 1
        return i
