# First Letter to Appear Twice

class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        x =set()
        for i in s:
            if i in x:
                return i
            else:
                x.add(i)