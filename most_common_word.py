ifrom collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.split('\W+', paragraph.lower())
        return Counter(w for w in words if w not in banned).most_common(1)[0][0]
        

