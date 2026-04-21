# Single Number

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = 0
        for x in nums:
            d=d^x
        return d