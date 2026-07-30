class Solution:
    def topKFrequent(self, nums, k):
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)

        out = []
        for freq in range(len(buckets) - 1, 0, -1): # decreasing order
            if buckets[freq]:
                for b in buckets[freq]:
                    out.append(b)
                    k = k - 1
                    if k == 0:
                        return out
        return out
