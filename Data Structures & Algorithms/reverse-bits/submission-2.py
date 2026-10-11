class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range(0,32):
            out <<= 1
            b = n % 2
            n >>= 1
            out |= b
        return out
