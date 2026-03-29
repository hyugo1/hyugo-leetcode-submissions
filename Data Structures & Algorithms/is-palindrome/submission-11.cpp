class Solution {
public:
    bool isPalindrome(string s) {
        // istringstream iss(s);
        char ch;
        string letter;
        for (int i = 0; i < s.size(); i++) {
            if (isalnum(s[i])) {
                letter += tolower(s[i]);
            }
        }
        std::cout << letter << endl;
        int l = 0;
        int r = letter.size() - 1;
        while (l < r) {
            if (letter[l] != letter[r]) {
                return false;
            }
            l++;
            r--;
        }

        return true;
    }
};
