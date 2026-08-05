
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, hi = 0, len(nums) - 1
        # compare mid against hi to find which half holds the rotation point (the min)
        # e.g., [3,4,1,2]: mid=4 > hi=2 -> min is right of mid, so low = mid+1
        while low < hi:
            mid = (low + hi) // 2
            if nums[mid] > nums[hi]: # left half is sorted, min is strictly to the right
                low = mid + 1
            else:                    # min is at mid or to its left; keep mid as candidate
                hi = mid
        return nums[low]
