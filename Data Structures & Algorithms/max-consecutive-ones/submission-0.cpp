class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int res = 0;
        int i = 0;
        while (i < nums.size()) {
            int temp = 0;
            while (i < nums.size() && nums[i] == 1) {
                temp++;
                res = max(res, temp);
                i++;
            }
            i++;
        }
        return res;
    }
};