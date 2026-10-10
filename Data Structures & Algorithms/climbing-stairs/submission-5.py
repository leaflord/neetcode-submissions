class Solution:
    def climbStairs(self, n: int, hist = None) -> int:
        if not hist:
            hist = {1:1,2:2}
        if n < 1:
            return 0
        elif n in hist:
            return hist[n]
        res = self.climbStairs(n - 1, hist) + self.climbStairs(n - 2, hist)
        hist[n] = res
        return res
        