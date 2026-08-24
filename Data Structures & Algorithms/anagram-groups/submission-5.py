class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for x in strs:
            x_sort = str(sorted(x))
            if x_sort in d:
                d[x_sort].append(x)
            else:
                d[x_sort]=[x]
        res=[]
        for x in d:
            res.append(d[x])
        return res
