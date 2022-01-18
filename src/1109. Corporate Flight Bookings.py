class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        diff = [0 for _ in range(n)]
        answer = [0 for _ in range(n)]
        for book in bookings:
            diff[book[0] - 1] += book[2]
            if book[1] < n:
                diff[book[1]] -= book[2]
        answer[0] = diff[0]
        for i in range(1, n):
            answer[i] = answer[i - 1] + diff[i]
        return answer
