# Palindrome Number

class Solution(object):
    def isPalindrome(self, x):
        temp = str(x)
        if str(x) == temp[::-1]:
            return True
        else:
            return False
        