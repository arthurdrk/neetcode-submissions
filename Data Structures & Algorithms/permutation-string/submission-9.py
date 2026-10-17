class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        def count(s):
            res = [0]*26
            for x in s:
                res[ord(x)-ord("a")]+=1
            return res
        c1 = count(s1)
        for i in range(len(s2)-len(s1)+1):
            substring = s2[i:i+len(s1)]
            if count(substring)==c1:
                return True
        return False