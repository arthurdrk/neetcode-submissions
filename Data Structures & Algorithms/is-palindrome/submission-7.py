class Solution:
    def isPalindrome(self, s: str) -> bool:
        # On garde seulement les caractères alphanumériques, en minuscule
        cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
        # On compare avec la version inversée
        return cleaned == cleaned[::-1]