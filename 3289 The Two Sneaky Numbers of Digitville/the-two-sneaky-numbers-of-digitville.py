class Solution(object):
    def getSneakyNumbers(self, nums):
        nums.sort()
        result = []
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                result.append(nums[i + 1])
            i = i + 1
        return result