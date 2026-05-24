# Sum of Values at Indices With K Set Bits

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans=[0]*(len(nums))

        for i in range(1,len(nums)):
            ans[i] = ans[i>>1] + (i&1)
        total=0
        for i in range(len(ans)):
            if ans[i] == k:
                total+=nums[i]
        return total
