class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for x in strs:
            classe = str(sorted(x))
            if classe in d:
                d[classe].append(x)
            else:
                d[classe]=[x]
        return [x for x in d.values()]



