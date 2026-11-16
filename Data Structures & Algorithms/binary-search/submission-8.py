class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)
        while l < h:
            m = (l + h)//2
            if target == nums[m]:
                return m
            elif nums[m] > target:
                h = m
            else:
                l = m + 1
        if nums[l - 1] == target:
            return l - 1
        return -1
