# Concatenation of Array

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = nums[::]
        for i in nums:
            s.append(i)
        return s