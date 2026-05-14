# Remove Outermost Parentheses

class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        balance = 0
        result = []
        for i in s:
            if i == '(':
                if balance>0:
                    result.append(i)
                balance+=1
            else:
                balance-=1
                if balance>0:
                    result.append(i)
        return ''.join(result)