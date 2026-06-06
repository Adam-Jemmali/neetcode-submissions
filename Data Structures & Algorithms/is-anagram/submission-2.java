

class Solution {
    public boolean isAnagram(String s, String t) {
        
        if(s.length() != t.length()) {
            return false;
        }

     
        Set<Character> checkedchar = new HashSet<>();

        String combined = t + s;

        for(int i = 0; i < combined.length(); i++) {
          
            char thechar = combined.charAt(i);
            
    
            if(checkedchar.contains(thechar)) {
                continue;
            }
            checkedchar.add(thechar);

          
            int countofs = 0;
            int countoft = 0;

       
            for (int j = 0; j < s.length(); j++) {
                if(thechar == s.charAt(j)) {
                    countofs = countofs + 1;
                }
            }

            
            for (int j = 0; j < t.length(); j++) {
                if(thechar == t.charAt(j)) {
                    countoft = countoft + 1;
                }
            }
            
            
            if(countoft != countofs) {
                return false;
            }
        }
        
       
        return true;
    }
    
  
}

