class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=[str(x) for x in digits]
        n=int("".join(l))
        n+=1
        return [x for x in str(n)]
