class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hist = dict()
        for ss in s:
            if ss not in hist:
                hist[ss] = 1
            else:
                hist[ss] = hist[ss] + 1
        for tt in t:
            if hist.get(tt, 0) == 0:
                return False
            hist[tt] = hist[tt] - 1
        return True