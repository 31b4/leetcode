class Solution {  
public:  
    int minimumCoins(vector<int>& prices) {  
        int n = prices.size();  
          
        vector<int>dp(n+1);  
          
        for(int i=n-1; i>=0; i--){  
            dp[i]  = prices[i];  
            int nextI = i+1;  
            int val = INT_MAX;  
            for(int j=i+1; j<=min(n,i+nextI+1); j++){  
                val = min(dp[j], val);  
            }  
            if(val < INT_MAX)dp[i] += val;   
           
        }  
        return dp[0];  
    }  
};
