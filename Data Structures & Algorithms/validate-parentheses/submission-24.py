class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")":"(","]":"[","}":"{"}
        stack=[]
        for i in range(len(s)):
            if not s[i] in close_to_open:
                stack.append(s[i])

            if s[i] in close_to_open:
                if not stack:
                    return False
                t=stack.pop()
                if t!=close_to_open[s[i]]:
                    return False
        if stack:
            return False
        return True
        
            