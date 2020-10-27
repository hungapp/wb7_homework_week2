from collections import deque
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
        self.word = ''

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isWord = True
        node.word = word
        
    def bfs(self):
        q = deque()
        q.append(self.root)
        res = ''
        while q:
            root = q.popleft()
            for node in root.children.values():
                if node.isWord:
                    q.append(node)
                    if len(node.word) > len(res) or node.word < res:
                        res = node.word
        return res
            
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words_trie = Trie()
        for w in words:
            words_trie.insert(w)
        return words_trie.bfs()
            
