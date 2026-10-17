class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        d = {}
        for x in nums:
            if x in d:
                d[x]+=1
            else:
                d[x]=1

        t = sorted(d.keys(), key=lambda x: d[x])
        return t[len(t)-k:]