import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftprod=[1]*len(nums)
        rightprod=[1]*len(nums)

        curr=1
        for i in range(1,len(nums)):
            curr*=nums[i-1]
            leftprod[i]=curr

        curr=1
        for i in range(len(nums)-2, -1, -1):
            curr*=nums[i+1]
            rightprod[i]=curr
        
        return [rightprod[i]*leftprod[i] for i in range(len(nums))]
