class Solution:
    def isValid(self, s: str) -> bool:
        open_close = {"{":"}","[":"]","(":")"}
        stack = []
        for i in range(0,len(s)):
            if s[i] in open_close:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                last= stack.pop()
                if not s[i]==open_close[last]:
                    return False
        
        return (not stack)
