
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

from typing import List

class Solution:
    def twoSum_brute(self, nums: List[int], target: int) -> List[int]:
        """ 力づく """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum_2hash(self, nums: List[int], target: int) -> List[int]:
        """ 2 pass hash を用いた手法 """
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 

if __name__ == "__main__":
    x = Solution()
    r = x.twoSum_brute([2,7,11,15], 9)
    r = x.twoSum_2hash([2,7,11,15], 9)
    print(r)