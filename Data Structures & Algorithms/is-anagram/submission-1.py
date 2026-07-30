class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = {}
        lt = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            ls[s[i]] = ls.get(s[i], 0) + 1
            lt[t[i]] = lt.get(t[i], 0) + 1
        return ls == lt