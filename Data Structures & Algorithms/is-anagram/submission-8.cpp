class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        unordered_map<char, int> shashmap;
        unordered_map<char, int> thashmap;

        for (int i = 0; i < size(s); i ++) {
            shashmap[s[i]]++;
        }

        for (int j = 0; j < size(t); j++) {
            thashmap[t[j]]++;
        }

        return shashmap == thashmap;
        
    }
};
