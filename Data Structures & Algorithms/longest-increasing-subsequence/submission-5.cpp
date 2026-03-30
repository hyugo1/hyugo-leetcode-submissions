class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> DP(nums.size(), 1);
        int res =1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] < nums[j]) {
                    DP[i] = max(DP[i], 1 + DP[j]);
                    res = max(res, DP[i]);
                }
            }
        }
        return res;
    }
};
