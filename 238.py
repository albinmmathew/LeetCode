# Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero=nums.count(0)
        if zero>1:
            return [0]*len(nums)
        product=1
        for i in nums:
            if i !=0:
                product*=i
        p=[]
        for i in nums:
            if zero==1:
                if i!=0:
                    p.append(0)
                else:
                    p.append(product)
            else:
                p.append(product//i)     
        return p      