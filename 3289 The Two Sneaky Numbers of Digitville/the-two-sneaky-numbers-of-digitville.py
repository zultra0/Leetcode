class Solution(object):
    def getSneakyNumbers(self, nums):
        twoNumbers = []
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if not nums[i + 1] > nums[i]:
                twoNumbers.append(nums[i + 1])
            i = i + 1
        return twoNumbers