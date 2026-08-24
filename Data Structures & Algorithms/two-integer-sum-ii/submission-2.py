class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        n=len(numbers)
        for i in range(n):
            curr = target - numbers[i]
            if curr in d:
                return [d[curr]+1,i+1]
            d[numbers[i]]=i
