class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vu = set()
        for i in range(len(nums)):
            if nums[i] in vu:
                return True
            else:
                vu.add(nums[i])
        return False

