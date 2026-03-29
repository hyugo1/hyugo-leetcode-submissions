class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char, char> hashmap = {{'}' , '{'}, {')' , '('}, {']', '['}};

        for (char& ch : s) {
            // closed paranthesis, basically if ch in hashmap
            if (hashmap.count(ch)) {
                if (!st.empty() && st.top() == hashmap[ch]) {
                    st.pop();
                } else {
                    return false;
                }
            // open parenthesis, we can push as much as we like.
            } else {
                st.push(ch);
            }
        }
        return st.empty();
    }
};
