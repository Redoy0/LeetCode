class Solution {
public:  
//int N=10010;
int dp[10010];
int numOfCoin(vector<int>& v,int amt)
{
    if(amt==0) return 0;
    int ans=INT_MAX;

    for(int i=0; i<v.size(); i++)
    {
        if(amt-v[i]>=0)
        {
            int subAns=0;
            if(dp[amt-v[i]]!=-1)
                subAns = dp[amt-v[i]];
            else
                subAns=numOfCoin(v,amt-v[i]);

            if( subAns !=INT_MAX && subAns+1<ans)
                ans = subAns+1;

        }
    }
    return dp[amt]=ans;
}
    int coinChange(vector<int>& coins, int amount) {
        memset(dp,-1,sizeof(dp));
        int ans=numOfCoin(coins,amount);
        return ans==INT_MAX ? -1:ans;
    }
};