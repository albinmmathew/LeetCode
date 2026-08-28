# Set Mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s =set(nums)
        # for i in range(1,len(nums)+1):
        #     if i not in s:
        #         miss = i
        #         break
        ogsum= len(nums)*(len(nums)+1)//2
        miss=ogsum-sum(s)
        dup = sum(nums) - sum(s) 
        return [dup,miss]