class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        unordered_set<char> seen(allowed.begin(), allowed.end());
        int res  = 0;
        for (const string& word : words) {
            bool good = true;
            for (const auto& w : word) {
                if (seen.find(w) == seen.end()) {
                    good = false;
                    break;
                }
            }
            if (good == true) {
                res += 1;
            }
        }
        return res;
    }
};