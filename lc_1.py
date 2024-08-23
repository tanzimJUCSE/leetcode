class Solution(object):
    def twoSum(self, nums, target):
        hash_table = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in hash_table:
                return [i, hash_table[comp]]
            hash_table[num] = i
        return []