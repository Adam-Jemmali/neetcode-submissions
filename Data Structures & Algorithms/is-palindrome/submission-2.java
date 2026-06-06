class Solution {
    public boolean isPalindrome(String s) {

        //clean string

        StringBuilder s1= new StringBuilder();
        for (char c: s.toCharArray()){
            if(Character.isLetterOrDigit(c)){
                s1.append(Character.toLowerCase(c));


            }
        }

        boolean valid = true;
        
        // Option 1: Check palindrome including all characters (letters and numbers)
        for(int i = 0; i < (s1.length() / 2); i++) {
            if(s1.charAt(i) != s1.charAt((s1.length() - 1) - i)) {
                valid = false;
                break;
            }
        }
        return valid;


        
    }
}
