class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1]
        suffixes = [1]
        length = len(nums)
        for i in range(1, length, 1):
            prefixes.append(nums[i-1] * prefixes[-1])
            suffixes.insert(0, nums[length - i] * suffixes[0])
        return [prefixes[i] * suffixes[i] for i in range(len(nums))]