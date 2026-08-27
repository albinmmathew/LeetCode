# Max Consecutive Ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m =0
        count =0
        for i in nums:
            if i == 1:
                count+=1
            else:
                m=max(m,count)
                count = 0
        return max(m,count)