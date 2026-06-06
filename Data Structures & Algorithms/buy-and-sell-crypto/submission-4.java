class Solution {
    public int maxProfit(int[] prices) {
        
        int maxprofit=0;

        for(int i=0;i<prices.length;i++){
            int boughtcoin= prices[i];
            for(int j=i+1;j<prices.length;j++){

                int soldbitcoin=prices[j];
                int profit= soldbitcoin-boughtcoin;

                maxprofit= Math.max(profit,maxprofit);


            }
        }

        return maxprofit;
    }
}
