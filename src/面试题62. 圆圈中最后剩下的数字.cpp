class Solution {
public:
    void merge(vector<int>& A, int m, vector<int>& B, int n) {
        for(int i = m; i < m + n; i++)
            A[i] = B[i - m];
        sort(A.begin(), A.end());
    }
};
