class Solution {
    public int maxArea(int[] heights) {

        // ares is calculate from difference of pointers

        int res=0; //output only 1 number
        int L=0;
        int r= heights.length -1;

        while (L<r){
            
            //get minimum hegihts * the base of area
            int area= Math.min(heights[L],heights[r]) *(r-L);

            res=Math.max(res,area);


            if(heights[L]<heights[r]){
                L++;


            }
            else{
                r--;
            }
         


        }
        return res;





        
    }
}
