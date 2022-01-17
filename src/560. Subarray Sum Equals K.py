import collections

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # """
        #     前缀和
        # """
        # res = 0
        # n = len(nums)
        # preSum = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     preSum[i] = preSum[i - 1] + nums[i - 1]
        # for i in range(1, n + 1):
        #     for j in range(i):
        #         if preSum[i] - preSum[j] == k:
        #             res += 1
        # return res

        """
            前缀和+哈希优化
            for j in range(i)
                if sum0_i - sum0_j == k
                    res += 1
            移项得
            if sum0_j == sum0_i - k
                res += sum0_j的个数
        """
        n = len(nums)
        preSum = collections.defaultdict(int)
        preSum[0] = 1
        res = 0
        sum0_i = 0
        for i in range(n):
            sum0_i += nums[i]
            res += preSum[sum0_i - k]
            preSum[sum0_i] += 1
        return res