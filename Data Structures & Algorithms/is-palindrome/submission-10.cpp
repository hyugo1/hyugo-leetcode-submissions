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
        // while (iss >> ch) {
        //     // letter.push_back(ch);
        //     letter += ch;
        // }
        std::cout << letter << endl;

        // for (int i = 0; i < letter.size() / 2; i++) {
        int l = 0;
        int r = letter.size() - 1;
        while (l < r) {
            // int l = i;
            // int r = letter.size() - i;
            // std::cout << s[l] << endl;
            if (letter[l] != letter[r]) {
                return false;
            }
            l++;
            r--;
        }

        return true;
    }
};
