class Solution:
    def hammingWeight(self, n: int, memo: dict) -> int:
        curr, out = n, 0
        while curr != 0:
            if curr in memo:
                out += memo[curr]
                return out
            out += 1 if (curr & 0b1) else 0
            curr >>= 1
        memo[n] = out
        return out

    def countBits(self, n: int) -> List[int]:
        out = []
        memo = dict()
        for i in range(n+1):
            out.append(self.hammingWeight(i, memo))
        return out