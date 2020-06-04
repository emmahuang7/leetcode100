class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            new_index = abs(nums[i])-1
            nums[new_index] = -abs(nums[new_index])
        return [i+1 for i,num in enumerate(nums) if num>0]
