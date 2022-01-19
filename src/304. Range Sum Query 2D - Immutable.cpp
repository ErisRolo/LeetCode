class NumMatrix {

private:
    vector<vector<int> > preSum;

public:
    NumMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        preSum.resize(m + 1, vector<int>(n + 1));
        for(int i = 1; i < m + 1; i++) {
            for(int j = 1; j < n + 1; j++) {
                preSum[i][j] = preSum[i - 1][j] + preSum[i][j - 1] + matrix[i - 1][j - 1] - preSum[i - 1][j - 1];
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        return preSum[row2 + 1][col2 + 1] - preSum[row2 + 1][col1] - preSum[row1][col2 + 1] + preSum[row1][col1];
    }
};

