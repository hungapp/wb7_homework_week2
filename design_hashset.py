class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 10000
        self.set = [None] * self.cap
        
    def hash(self, key):
        return key % self.cap
    
    def add(self, key: int) -> None:
        if self.contains(key):
            return
        
        hash_key = self.hash(key)
        if not self.set[hash_key]:
            self.set[hash_key] = []
        self.set[hash_key].append(key)
        
        
    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        hash_key = self.hash(key)
        self.set[hash_key].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash_key = self.hash(key)
        if not self.set[hash_key]:
            return False
        for k in self.set[hash_key]:
            if k == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
