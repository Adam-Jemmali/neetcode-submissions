class Solution {
    public int maxProfit(int[] prices) {

        //max prof
        //prices = [10,1,5,6,7,1] output 6

        //buy at 10$ but at 1$ 

        int maxprofit=0;
        int l=0;
        int r=1;

        while(r<prices.length){

            if (prices[l]< prices[r]) {
                //if price is bought AT LOW PRICE GOOD! 

                int profit= prices[r]-prices[l];

                maxprofit= Math.max(maxprofit,profit);



            }
            if(prices[l]==prices[r] || prices[l]>prices[r]){

                l=r;
            }
            r++;


        }
        return maxprofit;

        


        
    }
}
