class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> hashmap;

        for (const char& c : magazine) {
            hashmap[c]++;
        }

        for (int i = 0; i < ransomNote.size(); i++) {
            if (!hashmap.count(ransomNote[i]) || hashmap[ransomNote[i]] <= 0) {
                return false;
            }
            hashmap[ransomNote[i]]--;
        }
        return true;
    }
}; 