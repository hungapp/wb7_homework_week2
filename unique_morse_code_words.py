from collections import defaultdict
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformation_map = defaultdict(int)
        for word in words:
            transformation = ''
            for c in list(word):
                morse_index = ord(c) - ord('a')
                transformation += morse_codes[morse_index]
            transformation_map[transformation] += 1
        return len(transformation_map)
