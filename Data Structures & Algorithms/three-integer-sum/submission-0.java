class Solution {
     public static List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Set<List<Integer>> uniqueTriplets = new HashSet<>();
        
        int n = nums.length;
        
        // Brute force: check all possible combinations of 3 numbers
        for (int i = 0; i < n - 2; i++) {           // First number
            for (int j = i + 1; j < n - 1; j++) {   // Second number  
                for (int k = j + 1; k < n; k++) {   // Third number
                    
                    // Check if the three numbers sum to zero
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        // Create triplet and sort it to handle duplicates
                        List<Integer> triplet = Arrays.asList(nums[i], nums[j], nums[k]);
                       

                        Collections.sort(triplet);
                        
                        // Add to set (automatically handles duplicates)
                        uniqueTriplets.add(triplet);
                    }
                }
            }
        }
        
        // Convert set to list - cleaner approach
        return new ArrayList<>(uniqueTriplets);
    }
    
}
