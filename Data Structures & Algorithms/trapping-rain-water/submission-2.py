class Solution:
    def trap(self, height: List[int]) -> int:
        left = list(accumulate(height,max))
        right = list(accumulate(height[::-1],max))[::-1]
        output=0
        for i in range(len(height)):
            output+=min(left[i],right[i])-height[i]
        return output