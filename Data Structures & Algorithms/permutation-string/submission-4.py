class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        t1 = "".join(sorted(s1))
        r = len(t1)
        for i in range(0,len(s2)-r+1):
            x = s2[i:i+r]
            if t1 == "".join(sorted(x)):
                return True
        return False

