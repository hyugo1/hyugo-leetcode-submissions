class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> dp(nums);
        int res = nums[0];
        for (int i = 1; i < nums.size(); i ++) {
            dp[i] = max(nums[i], nums[i] + dp[i - 1]);
            res = max(res, dp[i]);
        }
        return res;
    }
};
