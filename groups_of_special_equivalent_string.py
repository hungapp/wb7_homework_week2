class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def count(word):
            ans = [0] * 52
            for i, char in enumerate(word):
                ans[ord(char) - ord('a') + 26 * (i % 2)] += 1
            return tuple(ans)
        return len(set(count(word) for word in A))
