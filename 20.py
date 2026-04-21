# Valid Parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        top = -1
        stack = []
        for i in s:
            if (i == ')' and top !=-1 and stack[top]=='('):
                stack.pop()
                top-=1
            elif i == '}' and top !=-1 and stack[top]=='{':
                stack.pop()
                top-=1
            elif i == ']' and top !=-1 and stack[top]=='[':
                stack.pop()
                top-=1
            elif i in "({[":
                stack.append(i)
                top+=1
            else:
                return False
        return top == -1