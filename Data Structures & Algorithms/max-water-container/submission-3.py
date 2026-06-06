class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #  [1,7,2,5,4,7,3,6]

        res=0
        leftp=0
        r=len(heights)-1

        
        while leftp< r:
            #take minumum of height of  both lines so water doesnt fill if take MAX WRON
            area= min(heights[leftp],heights[r]) * (r - leftp)
            res=max(res,area)
            if heights[leftp] < heights[r] :
                leftp +=1
            else:
                r -=1
        return res




        