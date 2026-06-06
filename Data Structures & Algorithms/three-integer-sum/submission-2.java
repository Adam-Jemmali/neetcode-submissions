
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();  
        for(int i = 0; i < nums.length - 2; i++) {    
            if(i > 0 && nums[i] == nums[i-1]) {      
                continue; // skip duplicates for i
            }
            
            int L = i + 1;                           // Fix 4: Consistent case - L not l
            int r = nums.length - 1;

            while (L < r) {
                int sum = nums[i] + nums[L] + nums[r];

                if (sum < 0) {
                    L++;                             // Fix 5: L++ not l++
                }
                else if (sum > 0) {
                    r--;
                }
                if(sum==0) {
                    // sum == 0, found triplet
                    res.add(Arrays.asList(nums[i], nums[L], nums[r]));  // Fix 6: add() not append()
                    
                    // Skip duplicates for L and r
                    while(L < r && nums[L] == nums[L+1]) {    // Fix 7: L+1 not L-1 (skip forward duplicates)
                        L++;
                    }
                    while(L < r && nums[r] == nums[r-1]) {    // Fix 8: Also skip r duplicates
                        r--;
                    }
                    
                    L++;  // Move both pointers after finding valid triplet
                    r--;
                }
            }
        }
        return res;
    }
    
    // Test method

}