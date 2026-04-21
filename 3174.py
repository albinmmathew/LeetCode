# Clear Digits

class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in s:
            if stack and stack[-1].isalpha() and i.isdigit():
                stack.pop()
            elif i.isalpha():
                stack.append(i)
        return "".join(stack)

        