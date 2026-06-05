# Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # s=[]
        # for i in nums:
        #     if i not in s:
        #         s.append(i)
        #     else:
        #         return True
        # return False
        l=len(nums)
        s=set(nums)
        sl=len(s)
        if l==sl:
            return False
        else:
            return True