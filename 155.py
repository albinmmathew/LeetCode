# Min Stack

class MinStack(object):

    def __init__(self):
        self.s = []
        self.min = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.s.append(val)
        if not self.min or self.min[-1]>=val:
            self.min.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if(self.s.pop()==self.min[-1]):
            self.min.pop()      

    def top(self):
        """
        :rtype: int
        """
        if not self.s:
            return -1
        else:
            return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.min:
            return -1
        else:
            return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()