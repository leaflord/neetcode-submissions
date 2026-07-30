class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0
        while n != 0:
            if n & 0b1:
                out += 1
            n >>= 1
        return out
