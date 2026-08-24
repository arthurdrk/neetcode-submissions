class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        count=defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]]+=1
        
        for x in count:
            heapq.heappush(heap, (count[x],x))
        while len(heap)>k:
            heapq.heappop(heap)
        return [x for _,x in heap]
