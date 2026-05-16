# Intersection of Two Arrays II

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        out =[]
        if len(nums1)<len(nums2):
            for i in nums1:
                if i in nums2:
                    nums2.remove(i)
                    out.append(i)
        else:
            for i in nums2:
                if i in nums1:
                    nums1.remove(i)
                    out.append(i)
        return out