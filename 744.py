# Find Smallest Letter Greater Than Target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        high = len(letters)-1
        low = 0
        while low<=high:
            mid=(high+low)//2
            if letters[mid]>target and letters[mid-1]<=target :
                return letters[mid]
            elif letters[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return letters[0]
