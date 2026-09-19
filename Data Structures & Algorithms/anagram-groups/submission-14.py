class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for x in strs:
            d["".join(sorted(x))].append(x)
        return list(d.values())
