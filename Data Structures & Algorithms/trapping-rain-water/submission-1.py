class Solution:
    def trap(self, height: List[int]) -> int:
        # full fill then as you move subtract --> squeeze theorem
        # if not equal take the min of h_l and h_r as height
        # layer by layer and move l and r by heights i.e. heights[l]<=heights[r]: l+=1 ..... dont add til after check
        # when heights_l and heights_r are the same you can add 1*distance between l and r 
        
        l, r = 0, len(height)-1
        res = 0
        prevMin = 0
        
        while l<r: 

            minDiff = max(0, min(height[l], height[r])-prevMin)
           
            res+=minDiff*(r-l) #minDiff*(r-l) 8
            prevMin = min(height[l], height[r]) #=1
            print(f"Heights: L is {height[l]} ; R is {height[r]}")
            print(f"Res Pre subtraction: {res}")

            lidx = l
            ridx = r

            if height[l]<=height[r]:
                l+=1
                while height[l]==0:
                    l+=1
                res-=min(height[lidx],height[l]) 
            else:
                r-=1
                while height[r]==0:
                    r-=1
                res-=min(height[ridx],height[r]) 
            print(f"Res post subtraction: {res}")
            

        return res
        
       


          # else:
            #     res+=min(height[l], height[r])*(r-l)
            
            #print(res)