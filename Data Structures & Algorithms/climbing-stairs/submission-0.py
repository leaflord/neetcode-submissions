def climbStairs(n: int, total, memo ) -> int:
    # naive solution
    if total > n:
        return 0
    if total in memo.keys():
        return memo[total]
    res = climbStairs(n, total + 1, memo) + climbStairs(n, total + 2, memo)
    memo[total] = res
    return res


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {n: 1}
        # naive solution
        return climbStairs(n, 0, memo)
