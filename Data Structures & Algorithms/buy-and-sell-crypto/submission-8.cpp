class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res= 0;
        int buy = prices[0];
        for (int i = 0; i < prices.size(); i++) {
            int sell = prices[i];
            int profit = sell - buy;
            if (profit > 0) {
                res = max(res, profit);
            } else {
                buy = sell;
            }
        }
        return res;
    }
};
