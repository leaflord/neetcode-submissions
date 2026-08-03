class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0, len(numbers) - 1
        while i < j:
            piv = numbers[i] + numbers[j] - target
            if piv == 0:
                return [i+1,j+1]
            elif piv > 0:
                j -= 1
            else:
                i += 1
        return [-1,-1]
