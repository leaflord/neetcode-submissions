class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, hi = 0, len(nums)
        while low < hi:
            mid = (low + hi) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid] > target:
                hi = mid
            else:
                low = mid + 1
        if nums[low - 1] == target:
            return low - 1
        else:
            return -1