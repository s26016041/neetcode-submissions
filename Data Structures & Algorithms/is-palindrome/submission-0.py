class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ''.join(t.lower() for t in s if t.isalnum())
        textLegth = len(text)
        for i, t in enumerate(text):
            if t != text[textLegth - i - 1]:
                return False

        return True