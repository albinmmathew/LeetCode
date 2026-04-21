# Self Dividing Numbers

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        l = []
        for i in range(left,right+1):
            temp = i
            f = True
            while(temp!=0):
                rem = temp%10 
                if rem!=0 and i%rem==0:
                    temp= temp//10
                else:
                    f = False
                    break
            if f:
                l.append(i)
        return l