class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for k, target in enumerate(nums):
            if target > 0:
                break
            if k > 0 and target == nums[k - 1]:
                # k > 0 is needed for [0,0,0] sorta cases
                continue # dup check
            i = k + 1; j = len(nums) - 1
            while i < j:
                added = nums[i] + nums[j] + target
                if added < 0:
                    i+=1
                elif added > 0:
                    j-=1
                elif added == 0:
                    result.append([nums[i], nums[j], target])
                    j -= 1 # since used, skip these nums
                    i += 1 # must be increased outside the loop, else duplicate results possible
                    while nums[i] == nums[i-1] and i < j:
                        i += 1
        return result