class Solution {
    public boolean isPalindrome(String s) {

        StringBuilder cleaned= new StringBuilder();

        for(char c: s.toCharArray()){

            if(Character.isLetterOrDigit(c)){
                cleaned.append(Character.toLowerCase(c));
            }
        }
        //reverse() only in StringBuuilder
        String final2comp=cleaned.toString();
        
        return final2comp.equals(cleaned.reverse().toString());
        
    }
}
