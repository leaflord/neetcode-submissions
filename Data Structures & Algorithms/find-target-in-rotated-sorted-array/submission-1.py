
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, hi = 0, len(nums) - 1
        while low < hi:
            mid = (low + hi) // 2
            if nums[mid] > nums[hi]:
                low = mid + 1
            else:
                hi = mid
        return low

    def binSearch(self, nums: List[int], target: int) -> int:
        low, hi = 0, len(nums) - 1
        while low <= hi:
            mid = (low + hi) // 2
            piv = nums[mid]
            if piv == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                hi = mid - 1
        return -1

    def search(self, nums, target):
        offset = self.findMin(nums)
        out = self.binSearch(nums[:offset], target)
        if out != -1:
            return out
        out = self.binSearch(nums[offset:], target)
        return out + offset if out != -1 else -1