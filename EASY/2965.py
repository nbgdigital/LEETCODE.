class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count = [1] + [0] * len(grid)**2

        for r in grid:
            for n in r:
                count[n] += 1

        return(count.index(2),count.index(0))
        
