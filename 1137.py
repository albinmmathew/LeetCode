# N-th Tribonacci Number

class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0,1,1]
        if n>-1 and n<3:
            return t[n]
        elif n>2:
            for i in range (3,n+1):
                t.append(t[-3]+t[-2]+t[-1])
            return t[-1]
        
        return -1