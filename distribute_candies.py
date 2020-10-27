class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        candies_set = set(candies)
        return min(len(candies_set), len(candies) // 2)
