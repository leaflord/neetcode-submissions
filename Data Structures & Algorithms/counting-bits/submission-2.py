class Solution:
    def countBits(self, n: int) -> List[int]:
        hist = {0:0, 1:1}
        out = []
        for i in range(0,n+1):
            res = hist[i//2] + (i % 2)
            out.append(res)
            hist[i] = res
        return out