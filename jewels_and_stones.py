from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stone_map = Counter(list(S))
        res = 0
        for j in list(J):
            res += stone_map[j]
        return res
