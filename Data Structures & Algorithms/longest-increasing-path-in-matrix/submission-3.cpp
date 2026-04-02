class Solution {
    int maxres = 0;
    vector<vector<int>> dp;
    vector<vector<int>> directions = {{-1, 0}, {1, 0},
                                      {0, -1}, {0, 1}};

public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        dp = std::vector<std::vector<int>>(rows, vector<int>(cols, - 1));
        int maxres = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                maxres = max(dfs(matrix, r, c, -1), maxres);
            }
        }
        return maxres;
    }
private:
    int dfs(vector<vector<int>>& matrix, int r, int c, int prevalue) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        if (r < 0 || c < 0 || r >= rows || c >= cols || matrix[r][c] <= prevalue) {
            return 0;
        }
        if (dp[r][c] != -1) return dp[r][c];

        int res = 1;
        for (vector<int> d : directions) {
            res = max(res, 1 + dfs(matrix, r + d[0], c + d[1], matrix[r][c]));
        }
        dp[r][c] = res;
        maxres = max(maxres, res);
        return res;
    }
};
