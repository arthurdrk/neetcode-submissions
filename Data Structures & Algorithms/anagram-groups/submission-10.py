class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for mot in strs:
            count=[0]*26
            for x in mot:
                count[ord(x)-ord('a')]+=1
            count=tuple(count)
            if count in d:
                d[count].append(mot)
            else:
                d[count]=[mot]
        return list(d.values())