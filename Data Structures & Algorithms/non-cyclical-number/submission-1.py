class Solution:
    def isHappy(self, n: int, memo = None) -> bool:
        if memo is None:
            memo = set()
        if n == 1:
            return True
        if n in memo:
            return False
        memo.add(n)
        sumsqr = 0
        while n > 0:
            dig = n % 10
            sumsqr += dig * dig
            n = n // 10
        return self.isHappy(sumsqr, memo)