class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in d: 
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        return sorted(d, key=d.get, reverse=True)[:k]