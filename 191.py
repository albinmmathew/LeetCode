# Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        soln = 1
        while n!=1:
            if n%2 == 1:
                soln+=1
            n//=2
        return soln