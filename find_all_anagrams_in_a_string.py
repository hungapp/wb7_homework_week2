from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        start = 0
        char_freq = Counter(p)
        matched = 0
        for end, right_char in enumerate(s):
            if right_char in char_freq:
                char_freq[right_char] -= 1
                if char_freq[right_char] == 0:
                    matched += 1
            if matched == len(char_freq):
                result.append(start)
            if end >= len(p) - 1:
                left_char = s[start]
                if left_char in char_freq:
                    if char_freq[left_char] == 0:
                        matched -= 1
                    char_freq[left_char] += 1
                    
                start += 1
        return result

