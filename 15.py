# 3Sum

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        soln = []
        for x in range(len(nums)-2):
            if x > 0 and nums[x]==nums[x-1]:
                continue
            left =  x+1
            right = len(nums)-1
            a = nums[x]
            while left < right:
                b = nums[left]
                c = nums[right]
                s = a+b+c
                if s == 0:
                    soln.append([a,b,c])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
                elif s<0:
                    left+=1
                else:
                    right-=1
        return soln