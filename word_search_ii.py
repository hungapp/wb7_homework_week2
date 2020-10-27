class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isWord = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.num_words = len(words)
        res, trie = [], Trie()
        for w in words:
            trie.insert(w)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.root, i, j, '', res)
        
        return res
    
    def dfs(self, board: List[List[str]], node, i: int, j: int, path, res) -> None:
        if self.num_words == 0:
            return 
        
        if node.isWord:
            res.append(path)
            node.isWord = False
            self.num_words -= 1
            
            
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
            return 
        
#       check if current char is in Trie  
        curr_char = board[i][j]
        if curr_char not in node.children: 
            return
        
        board[i][j] = '#'
        
        for x, y in [[0,-1], [0,1], [1,0], [-1,0]]:
            self.dfs(board, node.children[curr_char], i+x, j+y, path+curr_char, res)
        
        board[i][j] = curr_char

