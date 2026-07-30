class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mem = {}
        curr = 0
        for i in nums:
            curr = min(i, curr)
            mem[i] = True

        out = 0
        currlen = 0
        while len(mem) != 0:
            if curr in mem:
                mem.pop(curr)
                currlen+=1
            else:
                out = max(out, currlen)
                currlen = 0
            curr += 1
        return max(out, currlen) # final iteration
