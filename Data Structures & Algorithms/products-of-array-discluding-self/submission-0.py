class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            t = nums.copy()
            t.pop(i)
            res.append(math.prod(t))
        return res
        