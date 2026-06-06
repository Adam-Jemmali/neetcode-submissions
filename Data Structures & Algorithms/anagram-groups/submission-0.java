class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

    HashMap <String,List<String>> map= new HashMap<>();

	for(String s: strs){
        char [] charindiv= s.toCharArray();
        Arrays.sort(charindiv);
        String skeysort= new String(charindiv);


        if(!map.containsKey(skeysort)){
            map.put(skeysort,new ArrayList<>());



        }

        map.get(skeysort).add(s);

     }
     return new ArrayList<>(map.values());
		
    }
}
