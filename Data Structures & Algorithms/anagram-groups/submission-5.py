
def hashof(string):
    res = [0] * 26
    for char in string:
        res[ord(char) - ord('a')] += 1
    return tuple(res)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for string in strs:
            h = hashof(string)
            store[h].append(string)
        return list(store.values())
