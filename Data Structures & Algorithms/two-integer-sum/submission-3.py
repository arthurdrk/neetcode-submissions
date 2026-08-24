class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        n=len(nums)
        for i in range(n):
            curr = target - nums[i]
            if curr in d:
                return [d[curr],i]
            d[nums[i]]=i