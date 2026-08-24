class Solution:

    def encode(self, strs: List[str]) -> str:
        res =''
        for x in strs:
            res  =  res + x + ";"
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        n=len(s)
        last=-1
        for i in range(n):
            if s[i]==";":
                res.append(s[last+1:i])
                last=i
        return res