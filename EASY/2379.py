class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        lptr = 0 
        rc = 0
        res = k
        
        n = len(blocks)
        

        for rptr in range(n):
            if blocks[rptr] == "W":
                rc += 1
            if rptr - lptr + 1 == k:
                res = min(res,rc)
                if blocks[lptr] == "W":
                    rc -= 1
                lptr += 1
            
            
        return res



        
