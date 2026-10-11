class Solution:
    def hammingWeight(self, n: int) -> int:
        bitcount = 0
        while n > 0:
            bitcount += n % 2
            n = n // 2
        return bitcount