# Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0 or x==1:
           return x
        high = x
        low = 0
        while high>=low:
            mid = (high+low)//2
            sq = mid*mid
            if x == sq:
                return mid
            elif x > sq:
                low=mid+1
            else:
                high=mid-1
        return high