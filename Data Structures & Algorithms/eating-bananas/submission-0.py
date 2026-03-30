class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        mink = 0
        while lo<= hi:
            target_k = (lo+hi)//2

            totaltime = 0 
            for pile in piles:
                totaltime += math.ceil(pile/target_k) 
            
            if totaltime<=h: #if total time is less than hours it takes to eat all piles then good, can proceed
                mink = target_k #can set k because we were able to finish all the piles with this k, but still need to check for possible lower.
                hi = target_k - 1
            else: #else means that k isn't fast enough to finish all piles, so move up low for bin search
                lo = target_k + 1 
                #no need to set k here because k wasn't feasible.
        return mink
                

            
       
        