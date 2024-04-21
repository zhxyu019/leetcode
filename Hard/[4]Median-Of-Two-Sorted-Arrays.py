class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_list = nums1 + nums2
        merged_list.sort()
        
        if len(merged_list) % 2 == 0:
            middle_index = len(merged_list) // 2
            median = (merged_list[middle_index -1] + merged_list[middle_index]) / 2.0
        else:
            middle_index = len(merged_list) // 2
            median = merged_list[middle_index]
        return median