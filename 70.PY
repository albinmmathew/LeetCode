# Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        f = [1,2]
        if n==1:
            return 1
        if n>2:
            while len(f)<n:
                f.append(f[-1]+f[-2])
        return f[-1]