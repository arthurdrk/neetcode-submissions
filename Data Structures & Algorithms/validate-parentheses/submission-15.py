class Solution:
    def isValid(self, s: str) -> bool:
        d = {"{":"}","(":")","[":"]"}
        t = []
        if len(s)%2!=0:
            return False
        for i in range(len(s)):
            if s[i] in d:
                t.append(s[i])
            else:
                if not t:
                    return False
                x = t.pop()
                if d[x]!=s[i]:
                    return False
        return True if not t else False

