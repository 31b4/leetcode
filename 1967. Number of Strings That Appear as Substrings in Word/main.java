class Solution {
    public int numOfStrings(String[] patterns, String word) {
        int res = 0;
        for(String e: patterns){
            if(word.contains(e)){
                res++;
            }
        }
        return res;
    }
}
