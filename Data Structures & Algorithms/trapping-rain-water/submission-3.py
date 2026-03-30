class Solution:
    def trap(self, height: List[int]) -> int:
        # full fill then as you move subtract --> squeeze theorem
        # if not equal take the min of h_l and h_r as height
        # layer by layer and move l and r by heights i.e. heights[l]<=heights[r]: l+=1 ..... dont add til after check
        # when heights_l and heights_r are the same you can add 1*distance between l and r 
        
        l, r = 0, len(height)-1
        res = 0
        currentLevel = 0
        
        while l<r: 

            heightDiff = max(0, min(height[l], height[r])-currentLevel)
           
            res+=heightDiff*(r-l) 
            currentLevel += heightDiff 

            if height[l]<=height[r]:
                res-=min(currentLevel,height[l]) 
                l+=1
                      
            else:
                res-=min(currentLevel,height[r]) 
                r-=1
                 
        return res
        
       

            # print(f"Heights: L is {height[l]} ; R is {height[r]}")
            # print(f"Res Pre subtraction: {res}")

          # else:
            #     res+=min(height[l], height[r])*(r-l)
            
            #print(res)