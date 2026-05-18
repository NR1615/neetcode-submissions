from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True   # duplicate found
            else:
                hashmap[nums[i]] = 1
        return False  # no duplicates