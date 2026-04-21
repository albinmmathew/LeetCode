# Reverse Vowels of a String

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = list(s)
        left = 0
        right = len(s)-1
        vowels = "aeiouAEIOU"
        while left<right:
            if st[left] in vowels and st[right] in vowels:
                st[left],st[right]= st[right],st[left]
                left =left+1
                right =right-1
            elif st[left] not in vowels:
                left=left+1
            elif st[right] not in vowels:
                right=right-1
        return "".join(st)