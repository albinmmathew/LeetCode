# Simplify Path

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        p=path.split('/')
        for a in p:
            if a:
                if stack and a == "..":
                    stack.pop()
                elif a == "." or a =="..":
                    continue
                else:
                    stack.append(a)
        # print(p)
        c = "/" + "/".join(stack)
        return c
        