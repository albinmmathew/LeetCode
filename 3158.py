# Find the XOR of Numbers Which Appear Twice

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        og = []
        xor = 0
        for i in nums:
            if i not in og:
                og.append(i)
            else:
                xor^=i
        return xor