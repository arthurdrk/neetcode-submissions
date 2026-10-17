class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for x in strs:
            res += str(len(x))
            res+="#"
            res+=x
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            longueur = int(s[i:j])
            res.append(s[j+1:j+1+longueur])
            i = j+1+longueur

        return res




