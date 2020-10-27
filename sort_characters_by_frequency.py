# O(n)
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(char*times for char, times in Counter(s).most_common())

# O(nlogn)
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = Counter(s)
        return ''.join(sorted(list(s), key = lambda x: (char_count[x], ord(x)), reverse = True))
