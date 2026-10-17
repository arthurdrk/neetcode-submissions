class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left,right = 0, len(heights)-1
        currMax = 0
        while left < right :
            volume = min(heights[left],heights[right])*(right - left)
            if volume > currMax:
                currMax=volume
            if heights[left]<=heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1
            
        return currMax