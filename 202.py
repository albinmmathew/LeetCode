# Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        temp = n
        l = set()
        while True:
            d=0
            while temp!=0:
                d=d+((temp%10) * (temp%10))
                temp//=10
            if d==1:
                return True
            elif d in l:
                return False
            else:
                if d//10==0 and d!=1 and d!=7:
                    return False
                elif d == 1:
                    return True
                else:
                    l.add(d)
                    temp=d
                    d=0