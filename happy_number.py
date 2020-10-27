class Solution:
    def isHappy(self, n: int) -> bool:
        result_set = set()
        while n != 1:
            new_n = 0
            for i in list(str(n)):
                new_n += int(i)**2
            if new_n in result_set:
                return False
            result_set.add(new_n)
            n = new_n
        return True
