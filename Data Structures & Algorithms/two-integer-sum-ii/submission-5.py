class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        left = 0
        right = len(numbers)-1
        while left < right:
            q = numbers[left] + numbers[right]
            if q > target:
                right-=1
            elif q< target :
                left+=1
            else:
                return [left+1,right+1]
