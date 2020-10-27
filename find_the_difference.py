from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in (Counter(t) - Counter(s)):
            return char
