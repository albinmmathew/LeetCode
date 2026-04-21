# Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        y = ""
        for i in s:
            if i.isalnum():
                y+=(i.lower())
        rev = y[::-1]
        print(rev)
        if(y == rev):
            return True
        else:
            return False