class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #  [1,7,2,5,4,7,3,6]

        res=0
        

        for i, n in enumerate(heights):
            r=len(heights)-1
            while i < r:
                area= min(n,heights[r]) * (r-i)
                res=max(res,area)
                if n < heights[r]:
                    break
                else:
                    r -=1
        return res


          


        