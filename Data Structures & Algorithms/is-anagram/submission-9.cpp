class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> sMap;
        unordered_map<char, int> tMap;

        if (s.size() != t.size()) {
            return false;
        }

        for (int i = 0; i < size(s); i ++) {
            sMap[s[i]]++;
            std::cout << s[i] << "\n";
            tMap[t[i]]++;
        }

        return sMap == tMap;
    }
};
