class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        vector<int> res(arr.size());
        int curr_big = -1;
        for (int i = arr.size() - 1; i >=0; i--) {
            if (i != 0) {
                curr_big = max(curr_big, arr[i]);
            } else {
                curr_big = -1;
            }
            res[i] = curr_big;
        }
        reverse(res.begin() + 1, res.end());
        reverse(res.begin(), res.end());
        // return res ? !res.empty() : arr;
        if (!res.empty()) {
            return res;
        } else {
            return arr;
        }
    }
};