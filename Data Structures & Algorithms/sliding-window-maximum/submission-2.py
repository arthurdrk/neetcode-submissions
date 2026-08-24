class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        n=len(nums)
        for i in range(n-k+1):
            t=nums[i:i+k]
            res.append(max(t))

        return res