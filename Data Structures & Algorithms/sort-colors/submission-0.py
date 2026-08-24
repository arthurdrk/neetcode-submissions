class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {'r':0,'b':0,'w':0}
        for i in range(len(nums)):
            if nums[i]==0:
                count['r']+=1
            if nums[i]==1:
                count['w']+=1
            if nums[i]==2:
                count['b']+=1
        nums[:count['r']]=[0 for i in range(count['r'])]
        nums[count['r']:count['r']+count['w']]=[1 for i in range(count['w'])]
        nums[count['r']+count['w']:]=[2 for i in range(count['b'])]
        return nums

