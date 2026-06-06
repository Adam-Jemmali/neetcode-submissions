class Solution {
    public int maxArea(int[] heights) {

        // ares is calculate from difference of pointers

        //for loop from i to j

        int res=0;
        for(int i=0;i<heights.length;i++){

            for(int j=i+1;j<heights.length;j++){

                int area= Math.min(heights[i],heights[j]) * (j-i);

                res=Math.max(res,area);


            }
        }
        return res;

    




        
    }
}
