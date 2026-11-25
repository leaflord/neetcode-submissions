from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], t: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        res = []
        kvs = sorted(freq.items(), key=lambda kv: -kv[1])
        return [kv[0] for kv in kvs[:t]]