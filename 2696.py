# Minimum String Length After Removing Substrings

class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack =[]
        for i in s:
            if stack and ( (stack[-1] == 'C' and i =='D') or (stack[-1]=='A' and i == 'B')):
                    stack.pop()
            else:
                stack.append(i)
        # print(stack)
        return len(stack)