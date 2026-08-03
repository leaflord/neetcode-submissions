class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        key = defaultdict(int)
        for c in s1:
            key[c] += 1

        i = 0
        while i <= len(s2) - len(s1):
            can = defaultdict(int)
            for j in range(len(s1)):
                can[s2[i+j]] += 1
            for k in key.keys():
                if key[k] != can[k]:
                    break
            else:
                return True
            i+=1
        return False