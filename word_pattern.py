class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        index_map = {}
        
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        
        for i in range(len(words)):
            char_key = 'char_{}'.format(pattern[i])
            char_word = 'word_{}'.format(words[i])
            
            if char_key not in index_map:
                index_map[char_key] = i
            if char_word not in index_map:
                index_map[char_word] = i
            
            if index_map[char_key] != index_map[char_word]:
                return False
        
        return True

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return len(set(zip(pattern, s.split()))) == len(set(s.split())) == len(set(list(pattern))) and len(pattern) == len(s.split())
