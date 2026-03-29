class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashmap; //val, index


        for (int i = 0; i < size(nums); i++) {
            hashmap[nums[i]] = i;
        }

        for (int i = 0; i < size(nums); i++) {
            int diff = target - nums[i];
            if (hashmap.count(diff) && hashmap[diff] != i) {
                // return {hashmap[diff], i};
                return {i, hashmap[diff]};
            }
        }
        return {};
    }
};
