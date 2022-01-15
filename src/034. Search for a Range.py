class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums:
            i = 0
            j = len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if target > nums[m]:
                    i = m + 1
                else:
                    j = m - 1
            if i >= len(nums) or nums[i] != target:
                l = -1
            else:
                l = i
            i = 0
            j = len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if target < nums[m]:
                    j = m - 1
                else:
                    i = m + 1
            if j < 0 or nums[j] != target:
                r = -1
            else:
                r = j
            return [l, r]
        else:
            return [-1, -1]
