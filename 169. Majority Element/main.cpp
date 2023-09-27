class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size() / 2;
        set<int> numsSet(nums.begin(), nums.end());
        for(int num : numsSet){
            if(count(nums.begin(), nums.end(), num) > n ){
                return num;
            }
        }
        return 0;
    }
};
