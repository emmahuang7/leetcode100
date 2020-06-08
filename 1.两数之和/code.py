  
#错误！！
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for idx,num in enumerate(nums):
            d[num] = idx
         # 不能遍历元素，只能遍历坐标
         #元素可能重复，没有办法处理
         #[3,3]和target=6的情况
        for num in nums:
            idx_a = d.get(target-num)
            if idx_a and idx_a != d[num]:
                return d[num],idx_a
        return None 

# 正确      
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for idx,num in enumerate(nums):
            d[num] = idx
        for idx in range(len(nums)):
            idx_a = d.get(target-nums[idx])
            if idx_a and idx_a != idx:
                return idx,idx_a
        return None 
