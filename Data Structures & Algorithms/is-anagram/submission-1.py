class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = sorted([i for i in s])
        y = sorted([m for m in t])
        
        return x==y