class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (s.size() > t.size()) {
            return false;
        }
        
        int l = 0;
        for (int i = 0; i < t.size(); i++) {
            if (s[l] == t[i]) {
                l++;
            }
            if (s.size() == l) {
                return true;
            }
        }
        return false;
    }
};