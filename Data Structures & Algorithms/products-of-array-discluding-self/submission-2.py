class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # each product fits 32-bit. but the total product may not.
        sz = len(nums)
        pref, suff, out = [1] * sz, [1] * sz, [1] * sz
        for i in range(1, sz, 1):
            pref[i] = pref[i-1] * nums[i-1]
        for i in range(sz - 2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        return [pref[i]*suff[i] for i in range(sz)]