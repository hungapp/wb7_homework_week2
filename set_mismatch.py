# not using multiset
iclass Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
#           while value at i is not equal to value at j (value at an index should equals to value at its expected index)
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        for i, n in enumerate(nums):
            if n - 1 != i:
                return [n, i + 1]

# using multiset
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_counter = {i: 0 for i in range(1, len(nums) + 1)}
        for n in nums:
            num_counter[n] += 1
        res = [0] *2
        for n in num_counter:
            if num_counter[n] == 2:
                res[0] = n
            elif num_counter[n] == 0:
                res[1] = n
        return res
