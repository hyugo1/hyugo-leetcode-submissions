class Solution {
public:
    // int[n] dp;

    int numDecodings(string s) {
        int n = s.size();
        unordered_map<int, int> dp;
        return dfs(0, s, dp);
    }
private:
    int dfs(int i, string& s, unordered_map<int, int>& dp) {
        if (i == s.size()) {
            return 1;
        }
        if (dp.count(i)) {
            return dp[i];
        }
        if (s[i] == '0') {
            return 0;
        }
        std::string last_num = "0123456";
        int res = dfs(i + 1, s, dp);
        if (i + 1 < s.size() && (s[i] == '1' || (s[i] == '2' && s[i + 1] <= '6'))) {
            res += dfs(i + 2, s, dp);
        }
        dp[i] = res;
        return res;
    }
};
