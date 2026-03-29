class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int res= 0 ;
        unordered_set<int> seen(nums.begin(), nums.end());


        for (const int& n : nums) {
            if (seen.find((n - 1)) == seen.end()) {
                int length = 1;
                while (seen.find(n + length) != seen.end()) {
                    length++;
                }

                res = max(res, length);
            }
        }

        return res;        
    }
};
