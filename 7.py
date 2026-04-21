# Reverse Integer

class Solution(object):
    def reverse(self, x):
        if (x> (-2**31) and x<(2**31)-1):
            rev = 0
            y=x
            if(x<0):
                x= x*-1
            while (x!=0):
                rev = rev*10 + x%10
                x = x//10
            if(y<0):
                rev= rev * -1
            if (rev> (-2**31) and rev<(2**31)-1):
                return rev
            else:
                return 0
        else:
            return 0