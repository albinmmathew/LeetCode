# Fibonacci Number
 
class Solution(object):
    def fib(self, n):
        f =[0,1]
        if(n == 0 or n ==1):
            return f[n]
        elif n>=2 and n<=30:
            while (True):
                for i in range(2,n+1):
                    a = f[i-2]+f[i-1]
                    f.append(a)
                return f[n]
        else:
            return 0