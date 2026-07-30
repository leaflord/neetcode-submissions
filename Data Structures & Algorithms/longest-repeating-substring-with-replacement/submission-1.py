class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        sliding window.
        start with L and R at first position
        condition is:
            can you homogenize string under k replacements?
            1. make a map of char to count (can be incrementally updated per step)
            2. check if TOTAL - MAX_CHAR_COUNT <= k
            2.a. if you can, grow the window (r++)
            2.b. if you can't, shrink the window (l++)
            3. thru each iteration, keep a max tracker variable
        """
        res = 0 # max valid window length
        l, r = 0, 0
        freq = defaultdict(int)
        maxfreq = 0
        size = 0
        while r < len(s):
            freq[s[r]] += 1
            maxfreq = max(freq[s[r]], maxfreq)
            while r - l + 1 - maxfreq > k:
                freq[s[l]] -=1
                l+=1
            res = max(res, r - l + 1)
            r += 1

        return res