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
            prevMin += minDiff #=1


            print(f"Heights: L is {height[l]} ; R is {height[r]}")
            print(f"Res Pre subtraction: {res}")

     

            if height[l]<=height[r]:
                res-=min(prevMin,height[l]) 
                l+=1
                
                
            else:
                res-=min(prevMin,height[r]) 
                r-=1
                 
            print(f"Res post subtraction: {res}")
            

        return res
        
       


          # else:
            #     res+=min(height[l], height[r])*(r-l)
            
            #print(res)