class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        
        for string in strs:
            res = [0] * 26
            for char in string:
                res[ord(char) - ord('a')] += 1
            store[tuple(res)].append(string)
        return list(store.values())
