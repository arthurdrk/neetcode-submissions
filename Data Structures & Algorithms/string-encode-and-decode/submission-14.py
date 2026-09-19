from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += f"{len(word)}#{word}"

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Chercher la fin du nombre
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # Le mot commence juste après "#"
            start = j + 1
            end = start + length

            res.append(s[start:end])
            i = end

        return res