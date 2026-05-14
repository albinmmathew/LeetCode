# Remove Duplicate Letters

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack =[]
        lastocc={}
        visited = set()
        for i in range(len(s)):
            lastocc[s[i]]=i
        
        for i in range(len(s)):
            if s[i] not in visited:
                while (stack and stack[-1] > s[i]) and lastocc[stack[-1]]>i:
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])
        return ''.join(stack)
            