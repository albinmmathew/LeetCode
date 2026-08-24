# Shuffle the Array

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        soln=[]
        for i in range(n):
            soln.append(nums[i])
            soln.append(nums[n+i])
        return soln    