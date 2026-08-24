class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in count1:
                count1[s[i]]+=1
            else:
                count1[s[i]]=1
        count2 = {}
        for i in range(len(s)):
            if t[i] in count2:
                count2[t[i]]+=1
            else:
                count2[t[i]]=1
        return count1 == count2
