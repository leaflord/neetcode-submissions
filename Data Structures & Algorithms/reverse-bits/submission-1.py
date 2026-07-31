class Solution:
    def reverseBits(self, n: int) -> int:
        curr, out = n, 0
        for i in range(32):
            out <<= 1
            out |= (curr & 0b1)
            curr >>= 1
        return out