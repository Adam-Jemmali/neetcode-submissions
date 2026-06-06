class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;  // Handle empty array
        
        Set<Integer> sett = new HashSet<>();
        for(int num : nums){
            sett.add(num);
        }
        
        int maxlength = 0;  
        
        for(int num : sett){
            // Start the sequence only at the beginning
            if(!sett.contains(num-1)){
                int current = num;
                int currentlen = 1;
                
                while(sett.contains(current + 1)){
                    current = current + 1;
                    currentlen++;
                }
                
                maxlength=Math.max(maxlength,currentlen); 
                //After processing [2,3,4,5]: maxlength = max(0,4) = 4
// After processing [10]: maxlength = max(4,1 the currentlen) = 4 (keeps the 4!)
//After processing [20]: maxlength = max(4,1 the currenlen) = 4  
            }
        }
        return maxlength;
    }
}