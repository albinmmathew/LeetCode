# Intersection of Two Arrays

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        set2 = set(nums2)
        for i in set(nums1):
            if i in set2 and i not in result:
                result.append(i)
        return result