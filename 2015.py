# Watering Plants II

class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        """
        :type plants: List[int]
        :type capacityA: int
        :type capacityB: int
        :rtype: int
        """
        
        left = 0
        right = len(plants)-1
        refill =0
        canA = capacityA
        canB = capacityB
        while(left<right):        
            if canA<plants[left]:
                refill +=1
                canA =capacityA
            canA-=plants[left]
            left+=1

            if canB<plants[right]:
                refill +=1
                canB =capacityB
            canB-=plants[right]            
            right-=1

            if left == right:
                if max(canA,canB) < plants[left]:
                    refill+=1
        return refill