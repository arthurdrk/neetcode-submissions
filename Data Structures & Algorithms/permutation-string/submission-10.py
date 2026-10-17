class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        if len(s2) < m:
            return False

        c1 = [0] * 26
        c2 = [0] * 26

        for char in s1:
            c1[ord(char) - ord("a")] += 1

        for j, char in enumerate(s2):
            # Ajouter le caractère qui entre
            c2[ord(char) - ord("a")] += 1

            # Retirer celui qui sort pour garder une taille de m
            if j >= m:
                c2[ord(s2[j - m]) - ord("a")] -= 1

            if j >= m - 1 and c1 == c2:
                return True

        return False