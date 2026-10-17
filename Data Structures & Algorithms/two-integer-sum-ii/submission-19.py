class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        while left < right:
            somme = numbers[left] + numbers[right]
            if somme > target:
                right-=1
            elif somme < target:
                left+=1
            else:
                return [left+1,right+1]
        