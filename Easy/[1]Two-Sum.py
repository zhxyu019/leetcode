class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_map = {}
        for index, num in enumerate(nums) :
            if target - num in index_map:
                return index_map[target - num], index
            index_map[num] = index
