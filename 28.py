# Find the Index of the First Occurrence in a String

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        n = len(needle) 

        if n > len(haystack):
            return -1
        for i in range(len(haystack) - n + 1):
            if haystack[i] == needle[0] and haystack[i+n-1] == needle[-1]:
                j=0
                while j<n and haystack[i+j] == needle[j]:
                    j=j+1
                if j==n:
                    return i
        return -1