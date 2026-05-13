# Check If Word Is Valid After Substitutions

class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for ch in s:
            if ch == 'c':
                if len(stack)<2 or stack.pop()!='b' or stack.pop()!='a':
                    return False
            else:
                stack.append(ch)
        return not stack

        # t = 'abc'
        # while t in s:
        #     s=s.replace(t,'')
        # if s:
        #     return False
        # else:
        #     return True