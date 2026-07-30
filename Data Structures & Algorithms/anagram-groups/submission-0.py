from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        anas = defaultdict(list)
        for s in strs:
            anas[getAna(s)].append(s)
        return list(anas.values())

def getAna(s):
    # tuple(sorted(s))
    out = [0] * 26
    for c in s:
        out[ord(c) - ord('a')] = out[ord(c) - ord('a')] + 1
    return tuple(out)
