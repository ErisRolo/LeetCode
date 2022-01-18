class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int 
        :rtype: bool
        """
        diff = [0 for _ in range(1001)]
        temp = [0 for _ in range(1001)]
        for trip in trips:
            diff[trip[1]] += trip[0]
            diff[trip[2]] -= trip[0]
        temp[0] = diff[0]
        for i in range(1, 1001):
            temp[i] = temp[i - 1] + diff[i]
        if max(temp)<=capacity:
            return True
        else:
            return False