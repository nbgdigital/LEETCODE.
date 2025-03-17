from typing import List
from math import sqrt

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def counting(t):
            count = 0
            for r in ranks:
                count += int(sqrt(t / r))
            return count
        
        lptr = 1
        rptr = min(ranks) * cars * cars
        result = 0

        while lptr <= rptr:
            mid = (lptr + rptr) // 2
            cardone = counting(mid)

            if cardone >= cars:
                result = mid
                rptr = mid - 1
            else:
                lptr = mid + 1
        
        return result
