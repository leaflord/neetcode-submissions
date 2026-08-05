class Solution:
    def getSum(self, ai: int, bi: int) -> int:
        carry = 0
        res = 0
        for i in range(32):
            a = (ai >> i) & 0b1
            b = (bi >> i) & 0b1
            res |= (a ^ b ^ carry) << i
            carry = (a & b) | (a & carry) | (b & carry)

        if res > 0x7FFFFFFF: # copied. negative flip.
            res = ~(res ^ 0xFFFFFFFF)
        return res