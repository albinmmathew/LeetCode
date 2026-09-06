# Maximum Repeating Substring

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        f = word
        count = 0
        while f in sequence:
            f+=word
            count+=1
        return count