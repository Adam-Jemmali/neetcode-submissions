class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;

        int [] res= new int[n];
        int [] postfix= new int[n];

        int [] prefix= new int [n];

        prefix[0]=1;
        postfix[n-1]=1;

        // [1,2,3,4]  pref array for before index products of elems
        // nums[0]=1 nothing before it so prefix[0]=1
        //prefix = [1,1,]
        //prefix[1] must be nums[1]

        for(int i=1;i<n;i++){
            prefix[i]=prefix[i-1] * nums[i-1];
        }
        for(int i=n-2; i>=0;i-- ){

            postfix[i]=postfix[i+1] * nums[i+1];

            //fill postfix of current i  with  nums[i of right before elem]
        }

        for ( int i=0;i<n;i++){
            res[i]= postfix[i] * prefix[i];
        }

        return res;


        
        
    }
}  
