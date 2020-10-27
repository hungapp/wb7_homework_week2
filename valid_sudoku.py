class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        return not any(x in seen or seen.add(x)
                      for i, row in enumerate(board)
                      for j, char in enumerate(row)
                      if char != '.'
                      for x in ((char, i), (j, char), (i//3, j//3, char))
                      )
