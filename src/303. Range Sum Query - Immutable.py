class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # self.preSum = [0] * (len(nums) + 1)
        # for i in range(1, len(self.preSum)):
        #     self.preSum[i] = self.preSum[i - 1] + nums[i - 1]

        # self.preSum = [0]
        # for i in range(1, len(nums) + 1):
        #     self.preSum.append(self.preSum[i - 1] + nums[i - 1])

        self.preSum = [0]
        for i, num in enumerate(nums):
            self.preSum.append(self.preSum[i] + num)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.preSum[right + 1] - self.preSum[left]



        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(left,right)


n = NumArray([-2, 0, 3, -5, 2, -1])
print(n.sumRange(0, 2))
print(n.sumRange(2, 5))
print(n.sumRange(0, 5))
