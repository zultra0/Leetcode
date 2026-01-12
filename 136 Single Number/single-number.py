from typing import List

class Solution:
    # Sorting Approach
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        twice = []
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                twice.append(nums[i])
            i = i + 1
        singleArray = list(dict.fromkeys(nums))
        singleNumber = 0
        for x in range(len(singleArray)):
            if singleArray[x] not in twice:
                singleNumber = singleArray[x]
        return singleNumber
    # Brute Force Approach
    # def singleNumber(self, nums: List[int]) -> int: # [4,1,2,1,2]
    #     twice = [] # [1,2]
    #     i = 0
    #     while i < len(nums) - 1:
    #         j = i + 1
    #         while j < len(nums):
    #             if nums[i] == nums[j]:
    #                 twice.append(nums[i])
    #             j += 1
    #         i +=1
    #     singleArray = list(dict.fromkeys(nums)) # [4,1,2]
    #     singleNumber = 0
    #     j = 0
    #     while j < len(singleArray):
    #         if singleArray[j] not in twice:
    #             singleNumber = singleArray[j]
    #         j += 1
    #     return singleNumber