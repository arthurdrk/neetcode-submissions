class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =[]
        d={}
        for x in strs:
            y=str(sorted(x))
            if y in d:
                d[y].append(x)
            else:
                d[y]=[x]
        return [d[x] for x in d]